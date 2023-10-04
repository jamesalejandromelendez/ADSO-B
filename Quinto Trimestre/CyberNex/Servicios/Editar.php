<?php
include("../Conexion.php");

$serID = $_POST['serID'];
$serNombre = $_POST['serNombre'];
$serDescripcion = $_POST['serDescripcion'];
$serCosto = $_POST['serCosto'];
$tipSerId = $_POST['tipSerId'];

$sql = "UPDATE tbServicios SET serNombre='$serNombre', serDescripcion='$serDescripcion', serCosto='$serCosto', tipSerId='$tipSerId' WHERE serID='$serID';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Servicios.php");
}
?>