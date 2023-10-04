<?php
include("../Conexion.php");

$resId = $_POST['resId'];
$usuDocumento = $_POST['usuDocumento'];
$resEstado = $_POST['resEstado'];
$resCantidadAdultos = $_POST['resCantidadAdultos'];
$resCantidadNiños = $_POST['resCantidadNiños'];
$resFechaIngreso = $_POST['resFechaIngreso'];
$resFechaSalida = $_POST['resFechaSalida'];
$habNumero = $_POST['habNumero'];

$sql = "UPDATE tbReserva SET usuDocumento='$usuDocumento', resEstado='$resEstado', resCantidadAdultos='$resCantidadAdultos', resCantidadNiños='$resCantidadNiños', resFechaIngreso='$resFechaIngreso', resFechaSalida='$resFechaSalida', habNumero='$habNumero' WHERE resId='$resId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Reserva.php");
}
?>