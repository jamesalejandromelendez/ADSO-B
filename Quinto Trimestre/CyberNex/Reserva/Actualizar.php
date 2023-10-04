<?php
include("../Conexion.php");

$resId = $_GET['resId'];

$sql = "SELECT * FROM tbReserva WHERE resId = '$resId';";
$consulta = mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar reserva</title>
</head>
<body>
    <h1>Editar reserva</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="resId" name="resId" value="<?= $row['resId'] ?>" placeholder="ID" required>
        <input type="number" id="usuDocumento" name="usuDocumento" value="<?= $row['usuDocumento'] ?>" placeholder="Documento del Usuario" required>
        <input type="text" id="resEstado" name="resEstado" value="<?= $row['resEstado'] ?>" placeholder="Estado" required>
        <input type="number" id="resCantidadAdultos" name="resCantidadAdultos" value="<?= $row['resCantidadAdultos'] ?>" placeholder="Cantidad de Adultos" required>
        <input type="number" id="resCantidadNiños" name="resCantidadNiños" value="<?= $row['resCantidadNiños'] ?>" placeholder="Cantidad de Niños" required>
        <input type="date" id="resFechaIngreso" name="resFechaIngreso" value="<?= $row['resFechaIngreso'] ?>" placeholder="Fecha de Ingreso" required>
        <input type="date" id="resFechaSalida" name="resFechaSalida" value="<?= $row['resFechaSalida'] ?>" placeholder="Fecha de Salida" required>
        <input type="number" id="habNumero" name="habNumero" value="<?= $row['habNumero'] ?>" placeholder="Número de Habitación" required>

        <input type="submit" value="Actualizar reserva">
    </form>
</body>
</html>