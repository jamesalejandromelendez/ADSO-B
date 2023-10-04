<?php
include("../Conexion.php");

$tipProId = $_POST['tipProId'];
$tipProCategoria = $_POST['tipProCategoria'];

$sql = "INSERT INTO tbTipoProducto (tipProId, tipProCategoria) VALUES ('$tipProId', '$tipProCategoria');";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./TP_Servicios.php");
}
?>