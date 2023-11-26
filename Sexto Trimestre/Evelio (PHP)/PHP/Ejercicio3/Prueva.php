<?php
require_once('Empleado.php'); //Importar una sola vez de modo obligatorio

//Creando la instancia de Empleado
$empleado1 = new Empleado('Luz', '25-3-2000');
$empleado2 = new Empleado('Jeimy', '11-8-1996');
$empleado3 = new Empleado('Steven', '20-4-2000');
$empleado4 = new Empleado('Brayan', '30-5-1990');
$empleado5 = new Empleado('Socorro', '30-4-2001');
$empleado6 = new Empleado('Angela', '20-6-1996');
$empleado7 = new Empleado('Lucia', '20-3-1980');
$empleado8 = new Empleado('Miguel Angel', '6-10-1975');
$empleado9 = new Empleado('Edward', '2-7-2000');
$empleado10 = new Empleado('Romeo', '1-11-1999');

//Objeto empleado invocando un método no estático clásico
$empleado1->metodoNoEstatico();

//Clase Empleado invocando a un método estático con el operador PHP ::
Empleado::metodoEstatico();

//Clase Empleado modificando su atributo estático $nacionalidad.
Empleado::$nacionalidad = 'colombiana';
echo "Tengo nacionalidad " . Empleado::$nacionalidad.'<br>';
//$empleado1->verFecha();
//$empleado1->verContador();