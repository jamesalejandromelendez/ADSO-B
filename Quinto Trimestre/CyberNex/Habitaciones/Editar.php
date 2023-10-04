<?php
include("../Conexion.php");

$habNumero = $_POST['habNumero'];
$habEstado = $_POST['habEstado'];
$habCaracteristicas = $_POST['habCaracteristicas'];
$habCostoBase = $_POST['habCostoBase'];
$habCapacidad = $_POST['habCapacidad'];
$habNroCamaSensilla = $_POST['habNroCamaSensilla'];
$habNroCamaDoble = $_POST['habNroCamaDoble'];
$habNroCamarotes = $_POST['habNroCamarotes'];
$tipHabId = $_POST['tipHabId'];

$sql = "UPDATE tbHabitacion SET habEstado='$habEstado', habCaracteristicas='$habCaracteristicas', habCostoBase='$habCostoBase', habCapacidad='$habCapacidad', habNroCamaSensilla='$habNroCamaSensilla', habNroCamaDoble='$habNroCamaDoble', habNroCamarotes='$habNroCamarotes', tipHabId='$tipHabId' WHERE habNumero='$habNumero';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Habitaciones.php");
}
?>