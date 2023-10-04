<?php
include("../Conexion.php");

$sql = "SELECT * FROM tbDetalleFactura";
$consulta = mysqli_query($conexion, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detalle de Factura CRUD</title>
</head>
<body>
    <h1>Crear detalle de factura</h1>
    <a href="../">Home</a>
    <form action="./Insertar.php" method="POST">
        <input type="number" id="facId" name="facId" placeholder="ID de Factura" required>
        <input type="number" id="resId" name="resId" placeholder="ID de Reserva" required>
        <input type="number" id="serId" name="serId" placeholder="ID de Servicio" required>
        <input type="number" id="detFacSubTotal" name="detFacSubTotal" step="0.01" placeholder="Subtotal" required>

        <input type="submit" value="Agregar detalle de factura">
    </form>

    <div>
        <h2>Detalles de factura registrados</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>ID de Factura</th>
                    <th>ID de Reserva</th>
                    <th>ID de Servicio</th>
                    <th>Subtotal</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <td><?= $row["detFacId"] ?></td>
                    <td><?= $row["facId"] ?></td>
                    <td><?= $row["resId"] ?></td>
                    <td><?= $row["serId"] ?></td>
                    <td><?= $row["detFacSubTotal"] ?></td>
                    <td><a href="./Actualizar.php?detFacId=<?= $row["detFacId"] ?>">Editar</a></td>
                    <td><a href="./Eliminar.php?detFacId=<?= $row["detFacId"] ?>">Eliminar</a></td>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>