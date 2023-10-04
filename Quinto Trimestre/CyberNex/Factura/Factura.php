<?php
include("../Conexion.php");

$sql = "SELECT * FROM tbFactura";
$consulta = mysqli_query($conexion, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factura CRUD</title>
</head>
<body>
    <h1>Crear factura</h1>
    <a href="../">Home</a>
    <form action="./Insertar.php" method="POST">
        <input type="date" id="facFecha" name="facFecha" placeholder="Fecha" required>
        <input type="number" id="facTotal" name="facTotal" step="0.01" placeholder="Total" required>

        <input type="submit" value="Agregar factura">
    </form>

    <div>
        <h2>Facturas registradas</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Fecha</th>
                    <th>Total</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <td><?= $row["facId"] ?></td>
                    <td><?= $row["facFecha"] ?></td>
                    <td><?= $row["facTotal"] ?></td>
                    <td><a href="./Actualizar.php?facId=<?= $row["facId"] ?>">Editar</a></td>
                    <td><a href="./Eliminar.php?facId=<?= $row["facId"] ?>">Eliminar</a></td>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>