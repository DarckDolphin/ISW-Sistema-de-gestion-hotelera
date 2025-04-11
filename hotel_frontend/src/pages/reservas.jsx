import { useEffect, useState } from 'react';
import API from '../api/axiosConfig';

function Reservas() {
  const [reservas, setReservas] = useState([]);
  const [form, setForm] = useState({
    fecha_entrada: '',
    fecha_salida: '',
    numero_huespedes: '',
    estado: 'pendiente',
    huesped: '',
    habitacion: '',
  });

  const fetchReservas = async () => {
    try {
      const res = await API.get('reservas/');
      setReservas(res.data);
    } catch (error) {
      alert('Error al cargar reservas');
    }
  };

  const crearReserva = async (e) => {
    e.preventDefault();
    try {
      await API.post('reservas/', form);
      fetchReservas();
      alert('Reserva creada');
    } catch (error) {
      alert('Error al crear reserva');
    }
  };

  const eliminarReserva = async (id) => {
    if (confirm('¿Eliminar esta reserva?')) {
      await API.delete(`reservas/${id}/`);
      fetchReservas();
    }
  };

  useEffect(() => {
    fetchReservas();
  }, []);

  return (
    <div>
      <h2>Reservas</h2>

      <form onSubmit={crearReserva}>
        <input
          type="date"
          placeholder="Entrada"
          value={form.fecha_entrada}
          onChange={(e) => setForm({ ...form, fecha_entrada: e.target.value })}
        />
        <input
          type="date"
          placeholder="Salida"
          value={form.fecha_salida}
          onChange={(e) => setForm({ ...form, fecha_salida: e.target.value })}
        />
        <input
          type="number"
          placeholder="Nº de huéspedes"
          value={form.numero_huespedes}
          onChange={(e) => setForm({ ...form, numero_huespedes: e.target.value })}
        />
        <input
          type="text"
          placeholder="ID huésped"
          value={form.huesped}
          onChange={(e) => setForm({ ...form, huesped: e.target.value })}
        />
        <input
          type="text"
          placeholder="ID habitación"
          value={form.habitacion}
          onChange={(e) => setForm({ ...form, habitacion: e.target.value })}
        />
        <button type="submit">Crear reserva</button>
      </form>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Entrada</th>
            <th>Salida</th>
            <th>Huéspedes</th>
            <th>Estado</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {reservas.map((r) => (
            <tr key={r.id}>
              <td>{r.id}</td>
              <td>{r.fecha_entrada}</td>
              <td>{r.fecha_salida}</td>
              <td>{r.numero_huespedes}</td>
              <td>{r.estado}</td>
              <td>
                <button onClick={() => eliminarReserva(r.id)}>Eliminar</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Reservas;
