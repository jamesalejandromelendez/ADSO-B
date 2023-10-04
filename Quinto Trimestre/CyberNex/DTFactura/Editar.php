<?php
include("../Conexion.php");

$detFacId = $_POST['detFacId'];
$facId = $_POST['facId'];
$resId = $_POST['resId'];
$serId = $_POST['serId'];
$detFacSubTotal = $_POST['detFacSubTotal'];

$sql = "UPDATE tbDetalleFactura SET facId='$facId', resId='$resId', serId='$serId', detFacSubTotal='$detFacSubTotal' WHERE detFacId='$detFacId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./DTFactura.php");
}
?>