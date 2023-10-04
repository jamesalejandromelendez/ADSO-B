<?php
include("../Conexion.php");

$habNumero = $_GET['habNumero'];

$sql = "SELECT * FROM tbHabitacion WHERE habNumero = '$habNumero';";
$consulta = mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar habitación</title>
</head>
<body>
    <h1>Editar habitación</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="habNumero" name="habNumero" value="<?= $row['habNumero'] ?>" placeholder="Número" required>
        <input type="text" id="habEstado" name="habEstado" value="<?= $row['habEstado'] ?>" placeholder="Estado" required>
        <input type="text" id="habCaracteristicas" name="habCaracteristicas" value="<?= $row['habCaracteristicas'] ?>" placeholder="Características" required>
        <input type="text" id="habCostoBase" name="habCostoBase" value="<?= $row['habCostoBase'] ?>" placeholder="Costo Base" required>
        <input type="number" id="habCapacidad" name="habCapacidad" value="<?= $row['habCapacidad'] ?>" placeholder="Capacidad" required>
        <input type="number" id="habNroCamaSensilla" name="habNroCamaSensilla" value="<?= $row['habNroCamaSensilla'] ?>" placeholder="Número de Camas Sencillas" required>
        <input type="number" id="habNroCamaDoble" name="habNroCamaDoble" value="<?= $row['habNroCamaDoble'] ?>" placeholder="Número de Camas Dobles" required>
        <input type="number" id="habNroCamarotes" name="habNroCamarotes" value="<?= $row['habNroCamarotes'] ?>" placeholder="Número de Camarotes" required>
        <select id="tipHabId" name="tipHabId" required>
            <option value="">Seleccione Tipo de Habitación</option>
            <?php
            $tipHabConsulta = mysqli_query($conexion, "SELECT tipHabId, tipHabTipo FROM tbTipoHabitacion");
            while ($tipHabRow = mysqli_fetch_assoc($tipHabConsulta)) {
                $selected = ($tipHabRow["tipHabId"] == $row['tipHabId']) ? 'selected' : '';
                echo '<option value="' . $tipHabRow["tipHabId"] . '" ' . $selected . '>' . $tipHabRow["tipHabTipo"] . '</option>';
            }
            ?>
        </select>

        <input type="submit" value="Actualizar habitación">
    </form>
</body>
</html>