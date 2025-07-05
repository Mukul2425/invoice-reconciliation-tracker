import { useEffect, useState } from "react";
import { getDisputes, resolveDispute } from "./api";

function Disputes({ invoiceId, token }) {
  const [disputes, setDisputes] = useState([]);
  const [filter, setFilter] = useState("ALL");
  const [message, setMessage] = useState("");


  useEffect(() => {
    fetchDisputes();
  }, [invoiceId]);

  const fetchDisputes = async () => {
    try {
      const data = await getDisputes(invoiceId, token);
      setDisputes(data);
    } catch (err) {
      console.error("Error fetching disputes", err);
    }
  };

  const handleResolve = async (id) => {
    try {
      await resolveDispute(id, token);
      setMessage("Dispute marked as resolved.");

      fetchDisputes(); // refresh after update
      setTimeout(() => setMessage(""), 3000);
    } catch (err) {
      alert("Failed to resolve dispute");
    }
  };

  const filteredDisputes = disputes.filter((d) => {
    if (filter === "ALL") return true;
    return d.status === filter;
  });

  return (
    <div className="mt-2 ml-4 border-l pl-4">
      <h4 className="font-semibold">Disputes for Invoice #{invoiceId}</h4>

      <div className="my-2">
        <label className="mr-2">Filter:</label>
        <select value={filter} onChange={(e) => setFilter(e.target.value)} className="border px-2 py-1">
          <option value="ALL">All</option>
          <option value="PENDING">Pending</option>
          <option value="RESOLVED">Resolved</option>
        </select>
      </div>

      {filteredDisputes.length === 0 ? (
        <p>No disputes.</p>
      ) : (
        <ul className="space-y-2">
          {filteredDisputes.map((dispute) => (
            <li key={dispute.id} className="border p-2 rounded">
              <p><strong>Reason:</strong> {dispute.reason}</p>
              <p>
                <strong>Status:</strong>{" "}
                <span className={dispute.status === "PENDING" ? "text-yellow-600" : "text-green-600"}>
                    {dispute.status}
                </span>
                {" "} | <strong>Submitted:</strong> {new Date(dispute.created_at).toLocaleDateString()}
              </p>
              {dispute.status === "PENDING" && (
                <button
                  className="mt-1 bg-blue-500 text-white px-2 py-1 rounded text-sm"
                  onClick={() => handleResolve(dispute.id)}
                >
                  Mark as Resolved
                </button>
              )}
              {message && <p className="text-green-600">{message}</p>}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Disputes;
