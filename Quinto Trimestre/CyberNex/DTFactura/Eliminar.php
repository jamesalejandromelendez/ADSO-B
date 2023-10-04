<?php
include("../Conexion.php");

$detFacId = $_GET['detFacId'];

$sql = "DELETE FROM tbDetalleFactura WHERE detFacId='$detFacId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./DTFactura.php");
}
?>