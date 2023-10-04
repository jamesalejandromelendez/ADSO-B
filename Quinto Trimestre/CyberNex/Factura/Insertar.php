<?php
include("../Conexion.php");

$facFecha = $_POST['facFecha'];
$facTotal = $_POST['facTotal'];

$sql = "INSERT INTO tbFactura (facFecha, facTotal) VALUES ('$facFecha', '$facTotal');";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./Factura.php");
}
?>