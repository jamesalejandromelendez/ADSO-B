<?php
include("../Conexion.php");

$usuDocumento = $_POST['usuDocumento'];
$usuNombre =$_POST['usuNombre'];
$usuApellido =$_POST['usuApellido'];
$usuEmail =$_POST['usuEmail'];
$usuTelefono =$_POST['usuTelefono'];
$usuGenero =$_POST['usuGenero'];
$usuContraseña =$_POST['usuContraseña'];
$usuEstado =$_POST['usuEstado'];
$tipUsuId =$_POST['tipUsuId'];

$sql = "INSERT INTO tbUsuarios VALUES ('$usuDocumento', '$usuNombre', '$usuApellido', '$usuEmail', '$usuTelefono', '$usuGenero', '$usuContraseña', '$usuEstado', '$tipUsuId');";
$consulta =  mysqli_query($conexion, $sql);

if($consulta){
    header("Location: ./Clientes.php");
};

?>