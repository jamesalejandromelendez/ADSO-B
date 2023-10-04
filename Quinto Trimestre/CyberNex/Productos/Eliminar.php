<?php
include("../Conexion.php");

$proId = $_GET['proId'];

$sql = "DELETE FROM tbProductos WHERE proId='$proId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Productos.php");
}
?>