<?php
include("../Conexion.php");

$sql = "SELECT * FROM tbTipoUsuario";
$consulta = mysqli_query($conexion, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tipo de Usuario CRUD</title>
</head>
<body>
    <h1>Crear tipo de usuario</h1>
    <a href="../">Home</a>
    <form action="./Insertar.php" method="POST">
        <input type="number" id="tipUsuId" name="tipUsuId" placeholder="ID" required>
        <input type="text" id="tipUsuRol" name="tipUsuRol" placeholder="Rol" required>

        <input type="submit" value="Agregar tipo de usuario">
    </form>

    <div>
        <h2>Tipos de usuario registrados</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Rol</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <td><?= $row["tipUsuId"] ?></td>
                    <td><?= $row["tipUsuRol"] ?></td>
                    <td><a href="./Actualizar.php?tipUsuId=<?= $row["tipUsuId"] ?>">Editar</a></td>
                    <td><a href="./Eliminar.php?tipUsuId=<?= $row["tipUsuId"] ?>">Eliminar</a></td>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>