import { useState } from "react";
import { loginUser } from "./api";

function LoginForm({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const data = await loginUser(email, password);
      onLogin(data.access_token);
    } catch (err) {
      setError("Invalid credentials");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-2">
      <h2 className="text-xl font-bold">Login</h2>
      <input type="email" placeholder="Email" value={email}
        onChange={(e) => setEmail(e.target.value)} className="border p-2 w-full" required />
      <input type="password" placeholder="Password" value={password}
        onChange={(e) => setPassword(e.target.value)} className="border p-2 w-full" required />
      {error && <p className="text-red-500">{error}</p>}
      <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Login</button>
    </form>
  );
}

export default LoginForm;
