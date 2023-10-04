<?php
include("../Conexion.php");

$usuDocumento = $_GET['usuDocumento'];

$sql = "DELETE FROM tbUsuarios WHERE usuDocumento='$usuDocumento';";
$consulta =  mysqli_query($conexion, $sql);

if($consulta){
    header("Location: ./Clientes.php");
};


?>