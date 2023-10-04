<?php
include("../Conexion.php");

$detFacId = $_GET['detFacId'];

$sql = "SELECT * FROM tbDetalleFactura WHERE detFacId = '$detFacId';";
$consulta = mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar detalle de factura</title>
</head>
<body>
    <h1>Editar detalle de factura</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="detFacId" name="detFacId" value="<?= $row['detFacId'] ?>" placeholder="ID" required>
        <input type="number" id="facId" name="facId" value="<?= $row['facId'] ?>" placeholder="ID de Factura" required>
        <input type="number" id="resId" name="resId" value="<?= $row['resId'] ?>" placeholder="ID de Reserva" required>
        <input type="number" id="serId" name="serId" value="<?= $row['serId'] ?>" placeholder="ID de Servicio" required>
        <input type="number" id="detFacSubTotal" name="detFacSubTotal" step="0.01" value="<?= $row['detFacSubTotal'] ?>" placeholder="Subtotal" required>

        <input type="submit" value="Actualizar detalle de factura">
    </form>
</body>
</html>