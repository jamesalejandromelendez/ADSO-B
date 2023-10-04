<?php
include("../Conexion.php");

// Consulta para obtener los registros de la tabla tbTipoProducto
$sql = "SELECT * FROM tbTipoProducto";
$consulta = mysqli_query($conexion, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tipo de Producto CRUD</title>
</head>
<body>
    <h1>Crear tipo de producto</h1>
    <form action="./Insertar.php" method="POST">
        <input type="number" id="tipProId" name="tipProId" placeholder="ID" required>
        <input type="text" id="tipProCategoria" name="tipProCategoria" placeholder="Categoría" required>

        <input type="submit" value="Agregar tipo de producto">
    </form>

    <div>
        <h2>Tipos de producto registrados</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Categoría</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <td><?= $row["tipProId"] ?></td>
                    <td><?= $row["tipProCategoria"] ?></td>
                    <td><a href="./Actualizar.php?tipProId=<?= $row["tipProId"] ?>">Editar</a></td>
                    <td><a href="./Eliminar.php?tipProId=<?= $row["tipProId"] ?>">Eliminar</a></td>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>