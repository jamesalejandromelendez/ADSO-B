<?php
include("../Conexion.php");

$sql = "SELECT * FROM tbProductos";
$consulta = mysqli_query($conexion, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Productos CRUD</title>
</head>
<body>
    <h1>Crear producto</h1>
    <a href="../">Home</a>
    <form action="./Insertar.php" method="POST">
        <input type="number" id="proId" name="proId" placeholder="ID" required>
        <input type="text" id="proNombre" name="proNombre" placeholder="Nombre" required>
        <input type="text" id="proCosto" name="proCosto" placeholder="Costo" required>
        <select id="tipProId" name="tipProId" required>
            <option value="">Seleccione Tipo de Producto</option>
            <?php
            $tipProConsulta = mysqli_query($conexion, "SELECT tipProId, tipProCategoria FROM tbTipoProducto");
            while ($tipProRow = mysqli_fetch_assoc($tipProConsulta)) {
                echo '<option value="' . $tipProRow["tipProId"] . '">' . $tipProRow["tipProCategoria"] . '</option>';
            }
            ?>
        </select>

        <input type="submit" value="Agregar producto">
    </form>

    <div>
        <h2>Productos registrados</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Costo</th>
                    <th>Tipo de Producto</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <td><?= $row["proId"] ?></td>
                    <td><?= $row["proNombre"] ?></td>
                    <td><?= $row["proCosto"] ?></td>
                    <td><?= $row["tipProId"] ?></td>
                    <td><a href="./Actualizar.php?proId=<?= $row["proId"] ?>">Editar</a></td>
                    <td><a href="./Eliminar.php?proId=<?= $row["proId"] ?>">Eliminar</a></td>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>