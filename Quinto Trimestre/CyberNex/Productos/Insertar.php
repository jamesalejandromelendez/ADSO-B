<?php
include("../Conexion.php");

$proId = $_POST['proId'];
$proNombre = $_POST['proNombre'];
$proCosto = $_POST['proCosto'];
$tipProId = $_POST['tipProId'];

$sql = "INSERT INTO tbProductos (proId, proNombre, proCosto, tipProId) VALUES ('$proId', '$proNombre', '$proCosto', '$tipProId');";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Productos.php");
}
?>