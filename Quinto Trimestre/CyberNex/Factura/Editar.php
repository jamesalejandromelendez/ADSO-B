<?php
include("../Conexion.php");

$facId = $_POST['facId'];
$facFecha = $_POST['facFecha'];
$facTotal = $_POST['facTotal'];

$sql = "UPDATE tbFactura SET facFecha='$facFecha', facTotal='$facTotal' WHERE facId='$facId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Factura.php");
}
?>