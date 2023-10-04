<?php
include("../Conexion.php");

$resId = $_GET['resId'];

$sql = "DELETE FROM tbReserva WHERE resId='$resId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Reserva.php");
}
?>