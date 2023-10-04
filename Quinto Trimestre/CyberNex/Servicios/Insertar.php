<?php
include("../Conexion.php");

$serID = $_POST['serID'];
$serNombre = $_POST['serNombre'];
$serDescripcion = $_POST['serDescripcion'];
$serCosto = $_POST['serCosto'];
$tipSerId = $_POST['tipSerId'];

$sql = "INSERT INTO tbServicios (serID, serNombre, serDescripcion, serCosto, tipSerId) VALUES ('$serID', '$serNombre', '$serDescripcion', '$serCosto', '$tipSerId');";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Servicios.php");
}
?>