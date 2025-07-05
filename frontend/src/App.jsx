import { useState } from "react";
import { loginUser, registerUser } from "./api";
import Dashboard from "./dashboard";

function App() {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState("");
  const [fullName, setFullName] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState(null);
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isLogin) {
        const data = await loginUser(email, password);
        setToken(data.access_token);
        setMessage("Login successful!");
      } else {
        await registerUser(email, fullName, password);
        setMessage("User registered successfully! Please log in.");
        setIsLogin(true);
      }
    } catch (err) {
      setMessage("Operation failed. Check inputs or try again.");
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h1 className="text-xl font-bold mb-4">Invoice Tracker</h1>

      {!token ? (
        <>
          <form onSubmit={handleSubmit} className="space-y-3">
            <input
              type="email"
              placeholder="Email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="border p-2 w-full"
              required
            />
            {!isLogin && (
              <input
                type="text"
                placeholder="Full Name"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
                className="border p-2 w-full"
              />
            )}
            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="border p-2 w-full"
              required
            />
            <button type="submit" className="bg-blue-600 text-white px-4 py-2 w-full rounded">
              {isLogin ? "Login" : "Register"}
            </button>
          </form>
          <button
            className="text-blue-600 underline mt-2"
            onClick={() => setIsLogin(!isLogin)}
          >
            {isLogin ? "New user? Register here" : "Already have an account? Login"}
          </button>
          <p className="mt-4 text-sm text-red-600">{message}</p>
        </>
      ) : (
        <Dashboard token={token} />
      )}
    </div>
  );
}

export default App;
