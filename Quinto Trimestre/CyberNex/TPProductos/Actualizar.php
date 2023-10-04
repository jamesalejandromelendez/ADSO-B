<?php
include("../Conexion.php");

$tipProId = $_GET['tipProId'];

$sql = "SELECT * FROM tbTipoProducto WHERE tipProId = '$tipProId';";
$consulta = mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar tipo de producto</title>
</head>
<body>
    <h1>Editar tipo de producto</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="tipProId" name="tipProId" value="<?= $row['tipProId'] ?>" placeholder="ID" required>
        <input type="text" id="tipProCategoria" name="tipProCategoria" value="<?= $row['tipProCategoria'] ?>" placeholder="Categoría" required>

        <input type="submit" value="Actualizar tipo de producto">
    </form>
</body>
</html>