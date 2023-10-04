<?php
include("../Conexion.php");

$sql = "SELECT * FROM tbServicios";
$consulta = mysqli_query($conexion, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servicios CRUD</title>
</head>
<body>
    <h1>Crear servicio</h1>
    <a href="../">Home</a>
    <form action="./Insertar.php" method="POST">
        <input type="number" id="serID" name="serID" placeholder="ID" required>
        <input type="text" id="serNombre" name="serNombre" placeholder="Nombre" required>
        <input type="text" id="serDescripcion" name="serDescripcion" placeholder="Descripción" required>
        <input type="text" id="serCosto" name="serCosto" placeholder="Costo" required>
        <input type="text" id="tipSerId" name="tipSerId" placeholder="Tipo de Servicio" required>

        <input type="submit" value="Agregar servicio">
    </form>

    <div>
        <h2>Servicios registrados</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Descripción</th>
                    <th>Costo</th>
                    <th>Tipo de Servicio</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <td><?= $row["serID"] ?></td>
                    <td><?= $row["serNombre"] ?></td>
                    <td><?= $row["serDescripcion"] ?></td>
                    <td><?= $row["serCosto"] ?></td>
                    <td><?= $row["tipSerId"] ?></td>
                    <td><a href="./Actualizar.php?serID=<?= $row["serID"] ?>">Editar</a></td>
                    <td><a href="./Eliminar.php?serID=<?= $row["serID"] ?>">Eliminar</a></td>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>