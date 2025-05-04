import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/login";
import Dashboard from "./pages/dashboard";
import Reservas from "./pages/reservas";

function App() {
  return (
    <>
      <h1>Ya ya estoy aqui tanq</h1>
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/reservas" element={<Reservas />} />
        </Routes>
      </Router>
    </>
  );
}

export default App;
