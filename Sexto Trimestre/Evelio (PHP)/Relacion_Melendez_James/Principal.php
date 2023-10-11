<?php
require_once('Clases.php');

// creando instancias

//APRENDIZ
$Aprendiz1 = new Aprendiz('1032677434', 'Alejandro', 'Gómez', 'alejandro@example.com');
$Aprendiz2 = new Aprendiz('52747656', 'Valeria', 'Hernández', 'valeria@gmail.com');
$Aprendiz3 = new Aprendiz('1028466382', 'Roberto', 'Martínez', 'roberto@gmail.com');
$Aprendiz4 = new Aprendiz('1037428463', 'Daniela', 'López', 'daniela@gmail.com');
$Aprendiz5 = new Aprendiz('52878123', 'Carlos', 'Pérez', 'carlos@gmail.com');

$Aprendiz6 = new Aprendiz('123456789', 'Laura', 'Rodríguez', 'laura@example.com');
$Aprendiz7 = new Aprendiz('987654321', 'Mariana', 'Sánchez', 'mariana@gmail.com');
$Aprendiz8 = new Aprendiz('555666777', 'Luis', 'García', 'luis@yahoo.com');
$Aprendiz9 = new Aprendiz('888777666', 'Elena', 'Fernández', 'elena@hotmail.com');
$Aprendiz10 = new Aprendiz('111222333', 'Pedro', 'Díaz', 'pedro@gmail.com');

$Aprendiz11 = new Aprendiz('1032677434','James', 'Smith','James@homatil.com');
$Aprendiz12 = new Aprendiz('52747656', 'Joel', 'Brown', 'Joel@gmail.com');
$Aprendiz13 = new Aprendiz('1028466382', 'Jhon', 'Johnson', 'Jhon@gmail.com');
$Aprendiz14 = new Aprendiz('1037428463', 'Camilo', 'Williams', 'Camilo@gmail.com');
$Aprendiz15 = new Aprendiz('52878123', 'Ana', 'Davis', 'Ana@gmail.com');

// FICHA
$ficha1 = new Ficha('2560664B', '');
$ficha1->agregarAprendiz($aprendiz1);
$ficha1->agregarAprendiz($aprendiz2);
$ficha1->agregarAprendiz($aprendiz3);
$ficha1->agregarAprendiz($aprendiz4);
$ficha1->agregarAprendiz($aprendiz5);

$ficha2 = new Ficha('2560664A', '');
$ficha1->agregarAprendiz($aprendiz6);
$ficha1->agregarAprendiz($aprendiz7);
$ficha1->agregarAprendiz($aprendiz8);
$ficha1->agregarAprendiz($aprendiz9);
$ficha1->agregarAprendiz($aprendiz10);

$ficha3 = new Ficha('2560665B', '');
$ficha1->agregarAprendiz($aprendiz11);
$ficha1->agregarAprendiz($aprendiz12);
$ficha1->agregarAprendiz($aprendiz13);
$ficha1->agregarAprendiz($aprendiz14);
$ficha1->agregarAprendiz($aprendiz15);



//PROGRAMA
$progama1 = new Programa('218120', 'ADSO');
?>