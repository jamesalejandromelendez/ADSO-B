const express = require("express");
const app = express();
const mysql = require("mysql");
const cors = require("cors");

app.use(cors());
app.use(express.json());

//Conexión

const db = mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"",
    database:"db_hotel"
});

// Método registrar

app.post("/create",(req,res)=>{
    const id_usuario = req.body.id_usuario;
    const usuario = req.body.usuario;
    const nombre = req.body.nombre;
    const apellido = req.body.apellido;
    const correo = req.body.correo;
    const password = req.body.password;
    const id_tipo = req.body.id_tipo;

    // Query

    db.query("INSERT INTO datos_usuario(id_usuario, usuario, nombre, apellido, correo, password, id_tipo)VALUES(?,?,?,?,?,?,?)", [id_usuario, usuario, nombre, apellido, correo, password, id_tipo], (error, result) => {
        if (error) {
            console.log(error);
        } else {
            res.send("Registro exitoso")
        }
    }
    );

});

app.get("/usuarios",(req,res)=>{
    db.query('SELECT * FROM datos_usuario',
    (err,result)=>{
        if(err){
            console.log(err);
        }else{
            res.send(result);
        }
    });
});

app.put("/update",(req,res)=>{
    const id_usuario = req.body.id_usuario;
    const usuario = req.body.usuario;
    const nombre = req.body.nombre;
    const apellido = req.body.apellido;
    const correo = req.body.correo;
    const password = req.body.password;
    const id_tipo = req.body.id_tipo;

    db.query(
        'UPDATE datos_usuario SET usuario=?,nombre=?,apellido=?,correo=?,password=?,id_tipo=? WHERE id_usuario=?',[usuario,nombre,apellido,correo,password,id_tipo,id_usuario],
    (err,result)=>{
        if(err){
            console.log(err);
        }else{
            res.send(result);
        }
    }
    );
});

app.delete("/delete/:id_usuario",(req,res)=>{
    const id_usuario = req.params.id_usuario;

    db.query('DELETE FROM datos_usuario WHERE id_usuario=?', id_usuario,(err,result)=>{
        if(err){
            console.log(err);
        }else{
            res.send(result);
        }
    });
});

app.listen(3001,()=>{
    console.log("Puerto activo")
});