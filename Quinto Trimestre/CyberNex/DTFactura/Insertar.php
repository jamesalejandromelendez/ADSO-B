<?php
include("../Conexion.php");

$facId = $_POST['facId'];
$resId = $_POST['resId'];
$serId = $_POST['serId'];
$detFacSubTotal = $_POST['detFacSubTotal'];

$sql = "INSERT INTO tbDetalleFactura (facId, resId, serId, detFacSubTotal) VALUES ('$facId', '$resId', '$serId', '$detFacSubTotal');";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./DTFactura.php");
}
?>