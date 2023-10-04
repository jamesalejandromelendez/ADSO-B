<?php
include("../Conexion.php");

$tipUsuId = $_POST['tipUsuId'];
$tipUsuRol = $_POST['tipUsuRol'];

$sql = "INSERT INTO tbTipoUsuario (tipUsuId, tipUsuRol) VALUES ('$tipUsuId', '$tipUsuRol');";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./TPCliente.php");
}
?>