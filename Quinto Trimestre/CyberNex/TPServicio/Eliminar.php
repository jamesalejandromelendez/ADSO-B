<?php
include("../Conexion.php");

$tipProId = $_GET['tipProId'];

$sql = "DELETE FROM tbTipoProducto WHERE tipProId='$tipProId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./TP_Servicios.php");
}
?>