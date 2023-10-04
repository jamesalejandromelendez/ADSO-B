<?php
include("../Conexion.php");

$habNumero = $_GET['habNumero'];

$sql = "DELETE FROM tbHabitacion WHERE habNumero='$habNumero';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Habitaciones.php");
}
?>