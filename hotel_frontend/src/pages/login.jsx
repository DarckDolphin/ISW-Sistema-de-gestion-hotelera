import { useState } from 'react';
import axios from 'axios';

function Login() {
  const [form, setForm] = useState({ username: '', password: '' });

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:8000/api/token/', form);
      localStorage.setItem('access', res.data.access);
      localStorage.setItem('refresh', res.data.refresh);
      window.location.href = '/dashboard';
    } catch (err) {
      alert('Credenciales inválidas');
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <h2>Iniciar sesión</h2>
      <input
        type="text"
        placeholder="Usuario"
        value={form.username}
        onChange={(e) => setForm({ ...form, username: e.target.value })}
      />
      <input
        type="password"
        placeholder="Contraseña"
        value={form.password}
        onChange={(e) => setForm({ ...form, password: e.target.value })}
      />
      <button type="submit">Entrar</button>
    </form>
  );
}

export default Login;
