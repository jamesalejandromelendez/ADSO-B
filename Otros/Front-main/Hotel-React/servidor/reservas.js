// Importa las dependencias necesarias
const express = require("express");
const app = express();
const mysql = require("mysql");
const cors = require("cors");

app.use(cors());
app.use(express.json());

// Conexión a la base de datos (asegúrate de que estás utilizando los mismos detalles de conexión que usaste anteriormente)
const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "db_hotel"
});

// Ruta para crear una reserva
app.post("/reservas", (req, res) => {
  const { id_usuario, id_habitacion, num_personas, llegada, salida } = req.body;

  db.query(
    "INSERT INTO reservas (id_usuario, id_habitacion, num_personas, llegada, salida) VALUES (?, ?, ?, ?, ?)",
    [id_usuario, id_habitacion, num_personas, llegada, salida],
    (error, result) => {
      if (error) {
        console.log(error);
        res.status(500).json({ error: "Error al crear la reserva" });
      } else {
        res.status(201).json({ message: "Reserva creada con éxito" });
      }
    }
  );
});

// Ruta para obtener todas las reservas
app.get("/reservas", (req, res) => {
  db.query("SELECT * FROM reservas", (error, result) => {
    if (error) {
      console.log(error);
      res.status(500).json({ error: "Error al obtener las reservas" });
    } else {
      res.status(200).json(result);
    }
  });
});

// Ruta para actualizar una reserva
app.put("/reservas/:id", (req, res) => {
  const { id } = req.params;
  const { id_usuario, id_habitacion, num_personas, llegada, salida } = req.body;

  db.query(
    "UPDATE reservas SET id_usuario=?, id_habitacion=?, num_personas=?, llegada=?, salida=? WHERE id_reserva=?",
    [id_usuario, id_habitacion, num_personas, llegada, salida, id],
    (error, result) => {
      if (error) {
        console.log(error);
        res.status(500).json({ error: "Error al actualizar la reserva" });
      } else {
        res.status(200).json({ message: "Reserva actualizada con éxito" });
      }
    }
  );
});

// Ruta para eliminar una reserva
app.delete("/reservas/:id", (req, res) => {
  const { id } = req.params;

  db.query("DELETE FROM reservas WHERE id_reserva=?", id, (error, result) => {
    if (error) {
      console.log(error);
      res.status(500).json({ error: "Error al eliminar la reserva" });
    } else {
      res.status(200).json({ message: "Reserva eliminada con éxito" });
    }
  });
});

// Configura el servidor para escuchar en el puerto 3001
app.listen(3001, () => {
  console.log("Servidor activo en el puerto 3001");
});
