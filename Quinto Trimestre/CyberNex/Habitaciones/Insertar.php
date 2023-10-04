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

$sql = "INSERT INTO tbHabitacion (habNumero, habEstado, habCaracteristicas, habCostoBase, habCapacidad, habNroCamaSensilla, habNroCamaDoble, habNroCamarotes, tipHabId) VALUES ('$habNumero', '$habEstado', '$habCaracteristicas', '$habCostoBase', '$habCapacidad', '$habNroCamaSensilla', '$habNroCamaDoble', '$habNroCamarotes', '$tipHabId');";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Habitaciones.php");
}
?>