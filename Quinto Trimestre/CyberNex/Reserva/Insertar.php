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

$sql = "INSERT INTO tbReserva (resId, usuDocumento, resEstado, resCantidadAdultos, resCantidadNiños, resFechaIngreso, resFechaSalida, habNumero) VALUES ('$resId', '$usuDocumento', '$resEstado', '$resCantidadAdultos', '$resCantidadNiños', '$resFechaIngreso', '$resFechaSalida', '$habNumero');";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Reserva.php");
}
?>