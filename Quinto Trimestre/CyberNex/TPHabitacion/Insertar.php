<?php
include("../Conexion.php");

$tipHabId = $_POST['tipHabId'];
$tipHabTipo = $_POST['tipHabTipo'];

$sql = "INSERT INTO tbTipoHabitacion (tipHabId, tipHabTipo) VALUES ('$tipHabId', '$tipHabTipo');";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./TPHabitacion.php");
}
?>