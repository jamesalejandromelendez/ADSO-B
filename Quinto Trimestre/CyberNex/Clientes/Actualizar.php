<?php
include("../Conexion.php");

$usuDocumento = $_GET['usuDocumento'];

$sql = "SELECT * FROM tbUsuarios WHERE usuDocumento = '$usuDocumento';";
$consulta =  mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar usuarios</title>
</head>
<body>
    <h1>Editar usuario</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="" name="usuDocumento" value="<?= $row['usuDocumento']?>" placeholder="Documento" required>
        <input type="text" id="" name="usuNombre" value="<?= $row['usuNombre']?>" placeholder="Nombre">
        <input type="text" id="" name="usuApellido" value="<?= $row['usuApellido']?>" placeholder="Apellido">
        <input type="text" id="" name="usuEmail" value="<?= $row['usuEmail']?>" placeholder="Email">
        <input type="text" id="" name="usuTelefono" value="<?= $row['usuTelefono']?>" placeholder="Telefono">
        <input type="text" id="" name="usuGenero" value="<?= $row['usuGenero']?>" placeholder="Genero">
        <input type="text" id="" name="usuContraseña" value="<?= $row['usuContraseña']?>" placeholder="Contraseña">
        <input type="text" id="" name="usuEstado" value="<?= $row['usuEstado']?>" placeholder="Estado">
        <input type="number" id="" name="tipUsuId" value="<?= $row['tipUsuId']?>" placeholder="TipoUsuario">

        <input type="submit" value="Actualizar usuario">
    </form>

</body>
</html>