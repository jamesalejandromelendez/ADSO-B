<?php
include("../Conexion.php");

$serID = $_GET['serID'];

$sql = "SELECT * FROM tbServicios WHERE serID = '$serID';";
$consulta = mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar servicio</title>
</head>
<body>
    <h1>Editar servicio</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="serID" name="serID" value="<?= $row['serID'] ?>" placeholder="ID" required>
        <input type="text" id="serNombre" name="serNombre" value="<?= $row['serNombre'] ?>" placeholder="Nombre" required>
        <input type="text" id="serDescripcion" name="serDescripcion" value="<?= $row['serDescripcion'] ?>" placeholder="Descripción" required>
        <input type="text" id="serCosto" name="serCosto" value="<?= $row['serCosto'] ?>" placeholder="Costo" required>
        <input type="text" id="tipSerId" name="tipSerId" value="<?= $row['tipSerId'] ?>" placeholder="Tipo de Servicio" required>

        <input type="submit" value="Actualizar servicio">
    </form>
</body>
</html>