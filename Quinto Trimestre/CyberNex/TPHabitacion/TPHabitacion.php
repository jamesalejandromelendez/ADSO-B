<?php
include("../Conexion.php");

$sql = "SELECT * FROM tbTipoHabitacion";
$consulta = mysqli_query($conexion, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tipo de Habitación CRUD</title>
</head>
<body>
    <h1>Crear tipo de habitación</h1>
        <a href="../">Home</a>
    <form action="./Insertar.php" method="POST">
        <input type="number" id="tipHabId" name="tipHabId" placeholder="ID" required>
        <input type="text" id="tipHabTipo" name="tipHabTipo" placeholder="Tipo" required>

        <input type="submit" value="Agregar tipo de habitación">
    </form>

    <div>
        <h2>Tipos de habitación registrados</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Tipo</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <td><?= $row["tipHabId"] ?></td>
                    <td><?= $row["tipHabTipo"] ?></td>
                    <td><a href="./Actualizar.php?tipHabId=<?= $row["tipHabId"] ?>">Editar</a></td>
                    <td><a href="./Eliminar.php?tipHabId=<?= $row["tipHabId"] ?>">Eliminar</a></td>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>