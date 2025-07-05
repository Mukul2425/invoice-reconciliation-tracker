import { useState } from "react";
import { registerUser } from "./api";

function RegisterForm({ onRegister }) {
  const [email, setEmail] = useState("");
  const [fullName, setFullName] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    setError("");
    try {
      await registerUser(email, fullName, password);
      onRegister(); // switch to login view
    } catch (err) {
      setError("Registration failed. Try another email.");
    }
  };

  return (
    <form onSubmit={handleRegister} className="space-y-2">
      <h2 className="text-xl font-bold">Register</h2>
      <input type="email" placeholder="Email" value={email}
        onChange={(e) => setEmail(e.target.value)} className="border p-2 w-full" required />
      <input type="text" placeholder="Full Name" value={fullName}
        onChange={(e) => setFullName(e.target.value)} className="border p-2 w-full" required />
      <input type="password" placeholder="Password" value={password}
        onChange={(e) => setPassword(e.target.value)} className="border p-2 w-full" required />
      {error && <p className="text-red-500">{error}</p>}
      <button type="submit" className="bg-green-600 text-white px-4 py-2 rounded">Register</button>
    </form>
  );
}

export default RegisterForm;
