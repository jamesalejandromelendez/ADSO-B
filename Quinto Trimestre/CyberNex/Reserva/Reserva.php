<?php
include("../Conexion.php");

$sql = "SELECT * FROM tbReserva";
$consulta = mysqli_query($conexion, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reserva CRUD</title>
</head>
<body>
    <h1>Crear reserva</h1>
    <a href="../">Home</a>
    <form action="./Insertar.php" method="POST">
        <input type="number" id="resId" name="resId" placeholder="ID" required>
        <input type="number" id="usuDocumento" name="usuDocumento" placeholder="Documento del Usuario" required>
        <input type="text" id="resEstado" name="resEstado" placeholder="Estado" required>
        <input type="number" id="resCantidadAdultos" name="resCantidadAdultos" placeholder="Cantidad de Adultos" required>
        <input type="number" id="resCantidadNiños" name="resCantidadNiños" placeholder="Cantidad de Niños" required>
        <input type="date" id="resFechaIngreso" name="resFechaIngreso" placeholder="Fecha de Ingreso" required>
        <input type="date" id="resFechaSalida" name="resFechaSalida" placeholder="Fecha de Salida" required>
        <input type="number" id="habNumero" name="habNumero" placeholder="Número de Habitación" required>

        <input type="submit" value="Agregar reserva">
    </form>

    <div>
        <h2>Reservas registradas</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Documento del Usuario</th>
                    <th>Estado</th>
                    <th>Cantidad de Adultos</th>
                    <th>Cantidad de Niños</th>
                    <th>Fecha de Ingreso</th>
                    <th>Fecha de Salida</th>
                    <th>Número de Habitación</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <td><?= $row["resId"] ?></td>
                    <td><?= $row["usuDocumento"] ?></td>
                    <td><?= $row["resEstado"] ?></td>
                    <td><?= $row["resCantidadAdultos"] ?></td>
                    <td><?= $row["resCantidadNiños"] ?></td>
                    <td><?= $row["resFechaIngreso"] ?></td>
                    <td><?= $row["resFechaSalida"] ?></td>
                    <td><?= $row["habNumero"] ?></td>
                    <td><a href="./Actualizar.php?resId=<?= $row["resId"] ?>">Editar</a></td>
                    <td><a href="./Eliminar.php?resId=<?= $row["resId"] ?>">Eliminar</a></td>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>