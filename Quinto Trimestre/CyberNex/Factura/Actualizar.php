<?php
include("../Conexion.php");

$facId = $_GET['facId'];

$sql = "SELECT * FROM tbFactura WHERE facId = '$facId';";
$consulta = mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar factura</title>
</head>
<body>
    <h1>Editar factura</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="facId" name="facId" value="<?= $row['facId'] ?>" placeholder="ID" required>
        <input type="date" id="facFecha" name="facFecha" value="<?= $row['facFecha'] ?>" placeholder="Fecha" required>
        <input type="number" id="facTotal" name="facTotal" step="0.01" value="<?= $row['facTotal'] ?>" placeholder="Total" required>

        <input type="submit" value="Actualizar factura">
    </form>
</body>
</html>