<?php
include("../Conexion.php");

$tipUsuId = $_GET['tipUsuId'];

$sql = "SELECT * FROM tbTipoUsuario WHERE tipUsuId = '$tipUsuId';";
$consulta = mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar tipo de usuario</title>
</head>
<body>
    <h1>Editar tipo de usuario</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="tipUsuId" name="tipUsuId" value="<?= $row['tipUsuId'] ?>" placeholder="ID" required>
        <input type="text" id="tipUsuRol" name="tipUsuRol" value="<?= $row['tipUsuRol'] ?>" placeholder="Rol" required>

        <input type="submit" value="Actualizar tipo de usuario">
    </form>
</body>
</html>