import { useEffect, useState } from "react";
import { getInvoices, createInvoice, createDispute } from "./api";
import Disputes from "./Disputes"; // add at top




function Dashboard({ token }) {
  const [invoices, setInvoices] = useState([]);
  const [vendorName, setVendorName] = useState("");
  const [amount, setAmount] = useState("");
  const [disputeReasons, setDisputeReasons] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    if (token) fetchInvoices();
  }, [token]);

  const fetchInvoices = async () => {
    setLoading(true);
    try {
      const data = await getInvoices(token);
      setInvoices(data);
      setError("");
    } catch (err) {
      setError("Failed to fetch invoices");
    } finally {
      setLoading(false);
    }
  };

  const handleAddInvoice = async (e) => {
    e.preventDefault();
    if (!vendorName || !amount) return;

    try {
      await createInvoice(vendorName, parseFloat(amount), token);
      setVendorName("");
      setAmount("");
      setMessage("Invoice created!");
      setError("");
      fetchInvoices();
    } catch (err) {
      setError("Failed to create invoice");
      setMessage("");
    }
  };

  const handleDisputeChange = (invoiceId, value) => {
    setDisputeReasons((prev) => ({ ...prev, [invoiceId]: value }));
  };

  const handleCreateDispute = async (invoiceId) => {
    const reason = disputeReasons[invoiceId];
    if (!reason) return;

    try {
      await createDispute(invoiceId, reason, token);
      fetchInvoices(); // this refreshes dispute list
      setMessage(`Dispute submitted for invoice #${invoiceId}`);
      setError("");
      setDisputeReasons((prev) => ({ ...prev, [invoiceId]: "" }));
    } catch (err) {
      setError("Failed to submit dispute");
      setMessage("");
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">📄 Your Invoices</h2>

      {error && <p className="text-red-600 mb-2">{error}</p>}
      {message && <p className="text-green-600 mb-2">{message}</p>}

      <form onSubmit={handleAddInvoice} className="mb-6">
        <input
          type="text"
          placeholder="Vendor Name"
          value={vendorName}
          onChange={(e) => setVendorName(e.target.value)}
          className="border p-2 mr-2"
          required
        />
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          className="border p-2 mr-2"
          required
        />
        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded"
        >
          Add Invoice
        </button>
      </form>

      {loading ? (
        <p>Loading...</p>
      ) : invoices.length === 0 ? (
        <p>No invoices yet.</p>
      ) : (
        <ul className="space-y-4">
          {invoices.map((inv) => (
            <li key={inv.id} className="border p-4 rounded shadow-sm">
              <div className="mb-1">
                <strong>{inv.vendor_name}</strong> — ₹{inv.amount}
              </div>
              <div className="text-sm text-gray-600 mb-2">
                Invoice #: {inv.invoice_number} | Status: {inv.status}
              </div>
                <Disputes token={token} invoiceId={inv.id} />
              <input
                type="text"
                placeholder="Reason for dispute"
                value={disputeReasons[inv.id] || ""}
                onChange={(e) => handleDisputeChange(inv.id, e.target.value)}
                className="border p-1 mr-2 w-2/3"
              />
              <button
                onClick={() => handleCreateDispute(inv.id)}
                className="bg-red-600 text-white px-3 py-1 rounded"
              >
                Submit Dispute
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Dashboard;
