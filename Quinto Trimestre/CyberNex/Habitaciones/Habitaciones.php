<?php
include("../Conexion.php");

$sql = "SELECT * FROM tbHabitacion";
$consulta = mysqli_query($conexion, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Habitaciones CRUD</title>
</head>
<body>
    <h1>Crear habitación</h1>
    <a href="../">Home</a>
    <form action="./Insertar.php" method="POST">
        <input type="number" id="habNumero" name="habNumero" placeholder="Número" required>
        <input type="text" id="habEstado" name="habEstado" placeholder="Estado" required>
        <input type="text" id="habCaracteristicas" name="habCaracteristicas" placeholder="Características" required>
        <input type="text" id="habCostoBase" name="habCostoBase" placeholder="Costo Base" required>
        <input type="number" id="habCapacidad" name="habCapacidad" placeholder="Capacidad" required>
        <input type="number" id="habNroCamaSensilla" name="habNroCamaSensilla" placeholder="Número de Camas Sencillas" required>
        <input type="number" id="habNroCamaDoble" name="habNroCamaDoble" placeholder="Número de Camas Dobles" required>
        <input type="number" id="habNroCamarotes" name="habNroCamarotes" placeholder="Número de Camarotes" required>
        <select id="tipHabId" name="tipHabId" required>
            <option value="">Seleccione Tipo de Habitación</option>
            <?php
            $tipHabConsulta = mysqli_query($conexion, "SELECT tipHabId, tipHabTipo FROM tbTipoHabitacion");
            while ($tipHabRow = mysqli_fetch_assoc($tipHabConsulta)) {
                echo '<option value="' . $tipHabRow["tipHabId"] . '">' . $tipHabRow["tipHabTipo"] . '</option>';
            }
            ?>
        </select>

        <input type="submit" value="Agregar habitación">
    </form>

    <div>
        <h2>Habitaciones registradas</h2>
        <table>
            <thead>
                <tr>
                    <th>Número</th>
                    <th>Estado</th>
                    <th>Características</th>
                    <th>Costo Base</th>
                    <th>Capacidad</th>
                    <th>Número de Camas Sencillas</th>
                    <th>Número de Camas Dobles</th>
                    <th>Número de Camarotes</th>
                    <th>Tipo de Habitación</th>
                    <th></th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <?php
                    while($row = mysqli_fetch_assoc($consulta)):
                ?>

                <tr>
                    <td><?= $row["habNumero"] ?></td>
                    <td><?= $row["habEstado"] ?></td>
                    <td><?= $row["habCaracteristicas"] ?></td>
                    <td><?= $row["habCostoBase"] ?></td>
                    <td><?= $row["habCapacidad"] ?></td>
                    <td><?= $row["habNroCamaSensilla"] ?></td>
                    <td><?= $row["habNroCamaDoble"] ?></td>
                    <td><?= $row["habNroCamarotes"] ?></td>
                    <td><?= $row["tipHabId"] ?></td>
                    <td><a href="./Actualizar.php?habNumero=<?= $row["habNumero"] ?>">Editar</a></td>
                    <td><a href="./Eliminar.php?habNumero=<?= $row["habNumero"] ?>">Eliminar</a></td>
                </tr>
                <?php
                    endwhile;
                ?>
            </tbody>
        </table>
    </div>
</body>
</html>