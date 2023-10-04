<?php
include("../Conexion.php");

$proId = $_POST['proId'];
$proNombre = $_POST['proNombre'];
$proCosto = $_POST['proCosto'];
$tipProId = $_POST['tipProId'];

$sql = "UPDATE tbProductos SET proNombre='$proNombre', proCosto='$proCosto', tipProId='$tipProId' WHERE proId='$proId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Productos.php");
}
?>