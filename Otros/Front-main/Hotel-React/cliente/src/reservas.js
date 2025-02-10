import React, { useState, useEffect } from "react";
import Axios from "axios";
import Swal from "sweetalert2";
import 'bootstrap/dist/css/bootstrap.min.css';

function Reservas() {
  const [id_reserva, setIdReserva] = useState(0);
  const [id_usuario, setIdUsuario] = useState(0);
  const [id_habitacion, setIdHabitacion] = useState(0);
  const [num_personas, setNumPersonas] = useState(0);
  const [llegada, setLlegada] = useState("");
  const [salida, setSalida] = useState("");

  const [editar, setEditar] = useState(false);
  const [reservasList, setReservas] = useState([]);

  useEffect(() => {
    listarReservas();
  }, []);

  const listarReservas = () => {
    Axios.get("http://localhost:3001/reservas").then((response) => {
      setReservas(response.data);
    });
  }

  const addReserva = () => {
    Axios.post("http://localhost:3001/reservas", {
      id_usuario: id_usuario,
      id_habitacion: id_habitacion,
      num_personas: num_personas,
      llegada: llegada,
      salida: salida
    }).then(() => {
      listarReservas();
      clearForm();
      Swal.fire({
        title: "<strong>Reserva exitosa</strong>",
        html: "<i>La reserva fue creada con éxito</i>",
        icon: 'success',
        timer: 3000
      });
    }).catch((error) => {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: error.message === "Network error" ? "Intente más tarde" : error.message
      });
    });
  }

  const updateReserva = () => {
    Axios.put("http://localhost:3001/reservas/" + id_reserva, {
      id_usuario: id_usuario,
      id_habitacion: id_habitacion,
      num_personas: num_personas,
      llegada: llegada,
      salida: salida
    }).then(() => {
      listarReservas();
      clearForm();
      Swal.fire({
        title: "<strong>Actualización exitosa</strong>",
        html: "<i>La reserva fue actualizada con éxito</i>",
        icon: 'success',
        timer: 3000
      });
    }).catch((error) => {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: error.message === "Network Error" ? "Intente más tarde" : error.message
      });
    });
  }

  const deleteReserva = (val) => {
    Swal.fire({
      title: 'Confirmar eliminación',
      html: "<i>¿Realmente desea eliminar esta reserva?</i>",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Sí, eliminar'
    }).then((result) => {
      if (result.isConfirmed) {
        Axios.delete(`http://localhost:3001/reservas/${val.id_reserva}`).then(() => {
          listarReservas();
          clearForm();
          Swal.fire({
            icon: 'success',
            title: 'Reserva eliminada',
            showConfirmButton: false,
            timer: 2000
          });
        }).catch((error) => {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'No se logró eliminar la reserva',
            footer: error.message === "Network Error" ? "Intente más tarde" : error.message
          });
        });
      }
    });
  }

  const clearForm = () => {
    setIdReserva(0);
    setIdUsuario(0);
    setIdHabitacion(0);
    setNumPersonas(0);
    setLlegada("");
    setSalida("");
    setEditar(false);
  }

  const editarReserva = (val) => {
    setEditar(true);
    setIdReserva(val.id_reserva);
    setIdUsuario(val.id_usuario);
    setIdHabitacion(val.id_habitacion);
    setNumPersonas(val.num_personas);
    setLlegada(val.llegada);
    setSalida(val.salida);
  }

  return (
    <div className='container'>
      <div className='card text-center'>
        <div className='card-header'>
          GESTION DE RESERVAS
        </div>
        <div className='card-body'>
          <div className='formulario'>
            <h3>Datos de reserva</h3>
            <div className='info'>
              <label>ID Usuario</label>
              <input type='number' onChange={(event) => { setIdUsuario(event.target.value); }} className='form-control' value={id_usuario} />
            </div>
            <div className='info'>
              <label>ID Habitación</label>
              <input type='number' onChange={(event) => { setIdHabitacion(event.target.value); }} className='form-control' value={id_habitacion} />
            </div>
            <div className='info'>
              <label>Número de Personas</label>
              <input type='number' onChange={(event) => { setNumPersonas(event.target.value); }} className='form-control' value={num_personas} />
            </div>
            <div className='info'>
              <label>Fecha de Llegada</label>
              <input type='date' onChange={(event) => { setLlegada(event.target.value); }} className='form-control' value={llegada} />
            </div>
            <div className='info'>
              <label>Fecha de Salida</label>
              <input type='date' onChange={(event) => { setSalida(event.target.value); }} className='form-control' value={salida} />
            </div>
          </div>
          <div className='card-footer text-muted'>
            {
              editar ?
                <div>
                  <button className='btn btn-warning m-2' onClick={updateReserva}>Actualizar</button>
                  <button className='btn btn-info m-2' onClick={clearForm}>Cancelar</button>
                </div>
                :
                <button className='btn btn-success' onClick={addReserva}>Registrar</button>
            }
            <button className='btn btn-secondary' onClick={listarReservas}>Listar</button>
          </div>
        </div>
      </div>
      <div className='lista'>
        <table className="table table-striped">
          <thead>
            <tr>
              <th scope='col'>ID Reserva</th>
              <th scope='col'>ID Usuario</th>
              <th scope='col'>ID Habitación</th>
              <th scope='col'>Personas</th>
              <th scope='col'>Llegada</th>
              <th scope='col'>Salida</th>
              <th scope='col'>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {
              reservasList.map((val, key) => {
                return (
                  <tr key={val.id_reserva}>
                    <th>{val.id_reserva}</th>
                    <td>{val.id_usuario}</td>
                    <td>{val.id_habitacion}</td>
                    <td>{val.num_personas}</td>
                    <td>{val.llegada}</td>
                    <td>{val.salida}</td>
                    <td>
                      <div className="btn-group" role="group" aria-label="Basic example">
                        <button type="button" onClick={() => { editarReserva(val); }} className="btn btn-warning">Actualizar</button>
                        <button type="button" onClick={() => { deleteReserva(val); }} className="btn btn-danger">Eliminar</button>
                      </div>
                    </td>
                  </tr>
                );
              })
            }
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Reservas;