<?php
include("../Conexion.php");

$tipHabId = $_GET['tipHabId'];

$sql = "DELETE FROM tbTipoHabitacion WHERE tipHabId='$tipHabId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./TPHabitacion.php");
}
?>