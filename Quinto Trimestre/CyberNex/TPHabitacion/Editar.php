<?php
include("../Conexion.php");

$tipHabId = $_POST['tipHabId'];
$tipHabTipo = $_POST['tipHabTipo'];

$sql = "UPDATE tbTipoHabitacion SET tipHabTipo='$tipHabTipo' WHERE tipHabId='$tipHabId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./TPHabitacion.php");
}
?>