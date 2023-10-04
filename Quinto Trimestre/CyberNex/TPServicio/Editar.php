<?php
include("../Conexion.php");

$tipProId = $_POST['tipProId'];
$tipProCategoria = $_POST['tipProCategoria'];

$sql = "UPDATE tbTipoProducto SET tipProCategoria='$tipProCategoria' WHERE tipProId='$tipProId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./TP_Servicios.php");
}
?>