<?php
include("../Conexion.php");

$tipUsuId = $_GET['tipUsuId'];

$sql = "DELETE FROM tbTipoUsuario WHERE tipUsuId='$tipUsuId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./TPCliente.php");
}
?>