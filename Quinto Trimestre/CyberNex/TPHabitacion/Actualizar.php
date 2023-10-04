<?php
include("../Conexion.php");

$tipHabId = $_GET['tipHabId'];

$sql = "SELECT * FROM tbTipoHabitacion WHERE tipHabId = '$tipHabId';";
$consulta = mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar tipo de habitación</title>
</head>
<body>
    <h1>Editar tipo de habitación</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="tipHabId" name="tipHabId" value="<?= $row['tipHabId'] ?>" placeholder="ID" required>
        <input type="text" id="tipHabTipo" name="tipHabTipo" value="<?= $row['tipHabTipo'] ?>" placeholder="Tipo" required>

        <input type="submit" value="Actualizar tipo de habitación">
    </form>
</body>
</html>