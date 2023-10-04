<?php
include("../Conexion.php");

$proId = $_GET['proId'];

$sql = "SELECT * FROM tbProductos WHERE proId = '$proId';";
$consulta = mysqli_query($conexion, $sql);

$row = mysqli_fetch_assoc($consulta);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar producto</title>
</head>
<body>
    <h1>Editar producto</h1>
    <form action="./Editar.php" method="POST">
        <input type="hidden" id="proId" name="proId" value="<?= $row['proId'] ?>" placeholder="ID" required>
        <input type="text" id="proNombre" name="proNombre" value="<?= $row['proNombre'] ?>" placeholder="Nombre" required>
        <input type="text" id="proCosto" name="proCosto" value="<?= $row['proCosto'] ?>" placeholder="Costo" required>
        <select id="tipProId" name="tipProId" required>
            <option value="">Seleccione Tipo de Producto</option>
            <?php
            $tipProConsulta = mysqli_query($conexion, "SELECT tipProId, tipProCategoria FROM tbTipoProducto");
            while ($tipProRow = mysqli_fetch_assoc($tipProConsulta)) {
                $selected = ($tipProRow["tipProId"] == $row['tipProId']) ? 'selected' : '';
                echo '<option value="' . $tipProRow["tipProId"] . '" ' . $selected . '>' . $tipProRow["tipProCategoria"] . '</option>';
            }
            ?>
        </select>

        <input type="submit" value="Actualizar producto">
    </form>
</body>
</html>