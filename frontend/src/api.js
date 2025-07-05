const BASE_URL = import.meta.env.VITE_API_URL;

// Login
export async function loginUser(email, password) {
  const response = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      username: email,
      password: password,
    }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Login failed:", response.status, errorText);
    throw new Error("Login failed");
  }

  return await response.json();
}

// Register
export async function registerUser(email, fullName, password) {
  const response = await fetch(`${BASE_URL}/users/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      full_name: fullName,
      password,
    }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Registration failed:", response.status, errorText);
    throw new Error("Registration failed");
  }

  return await response.json();
}

// Get all invoices (for logged-in user)
export async function getInvoices(token) {
  const response = await fetch(`${BASE_URL}/invoices/`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Failed to fetch invoices:", response.status, errorText);
    throw new Error("Fetch failed");
  }

  return await response.json();
}

// Create invoice (for logged-in user)
export async function createInvoice(vendorName, amount, token) {
  const response = await fetch(`${BASE_URL}/invoices/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      vendor_name: vendorName,
      amount: amount,
    }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Invoice creation failed", response.status);
    console.error("Response body:", errorText);
    throw new Error("Create invoice failed");
  }

  return await response.json();
}
// Create dispute (for a given invoice)
export async function createDispute(invoiceId, reason, token) {
  const response = await fetch(`${BASE_URL}/dispute/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify({
      invoice_id: invoiceId,
      reason: reason,
    }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Dispute creation failed", response.status);
    console.error("Response body:", errorText);
    throw new Error("Create dispute failed");
  }

  return await response.json();
}

// Fetch disputes by invoice ID
export async function getDisputes(invoiceId, token) {
  const response = await fetch(`${BASE_URL}/invoices/${invoiceId}/disputes`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Failed to fetch disputes", response.status, errorText);
    throw new Error("Fetch disputes failed");
  }

  return await response.json();
}

// Resolve a dispute by ID
export async function resolveDispute(disputeId, token) {
  const response = await fetch(`${BASE_URL}/dispute/${disputeId}/resolve`, {
    method: "PUT",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  if (!response.ok) {
    const errorText = await response.text();
    console.error("Failed to resolve dispute", response.status, errorText);
    throw new Error("Resolve dispute failed");
  }

  return await response.json();
}
