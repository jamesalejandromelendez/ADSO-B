<?php
include("../Conexion.php");

$sql = "SELECT * FROM tbUsuarios;";
$consulta =  mysqli_query($conexion, $sql);
?>


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usuarios CRUD</title>
</head>
<body>
    <h1>Crear usuario</h1>
    <a href="../">Home</a>
    <form action="./Insertar.php" method="POST">
        <input type="number" id="" name="usuDocumento" placeholder="Documento" required>
        <input type="text" id="" name="usuNombre" placeholder="Nombre">
        <input type="text" id="" name="usuApellido" placeholder="Apellido">
        <input type="text" id="" name="usuEmail" placeholder="Email">
        <input type="text" id="" name="usuTelefono" placeholder="Telefono">
        <input type="text" id="" name="usuGenero" placeholder="Genero">
        <input type="text" id="" name="usuContraseña" placeholder="Contraseña">
        <input type="text" id="" name="usuEstado" placeholder="Estado">
        <input type="number" id="" name="tipUsuId" placeholder="TipoUsuario">

        <input type="submit" value="Agregar usuario">
    </form>

    <div>
        <h2>Usuarios registrados</h2>
        <table>
            <thead>
                <tr>
                    <th>Documento</th>
                    <th>Contraseña</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Email</th>
                    <th>Telefono</th>
                    <th>Genero</th>
                    <th>Estado</th>
                    <th>Tipo usuario</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <th><?= $row["usuDocumento"]?></th>
                    <th><?= $row["usuContraseña"]?></th>
                    <th><?= $row["usuNombre"]?></th>
                    <th><?= $row["usuApellido"]?></th>
                    <th><?= $row["usuEmail"]?></th>
                    <th><?= $row["usuTelefono"]?></th>
                    <th><?= $row["usuGenero"]?></th>
                    <th><?= $row["usuEstado"]?></th>
                    <th><?= $row["tipUsuId"]?></th>

                    <th><a href="./Actualizar.php?usuDocumento=<?= $row["usuDocumento"]?>">Editar</a></th>
                    <th><a href="./Eliminar.php?usuDocumento=<?= $row["usuDocumento"]?>">Eliminar</a></th>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>


    </div>



</body>
</html>