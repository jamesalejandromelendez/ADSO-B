<?php
include("../Conexion.php");

$serID = $_GET['serID'];

$sql = "DELETE FROM tbServicios WHERE serID='$serID';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Servicios.php");
}
?>