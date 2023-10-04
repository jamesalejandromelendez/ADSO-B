<?php
include("../Conexion.php");

$facId = $_GET['facId'];

$sql = "DELETE FROM tbFactura WHERE facId='$facId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Factura.php");
}
?>