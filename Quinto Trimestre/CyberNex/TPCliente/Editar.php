<?php
include("../Conexion.php");

$tipUsuId = $_POST['tipUsuId'];
$tipUsuRol = $_POST['tipUsuRol'];

$sql = "UPDATE tbTipoUsuario SET tipUsuRol='$tipUsuRol' WHERE tipUsuId='$tipUsuId';";
$consulta = mysqli_query($conexion, $sql);

if ($consulta) {
    header("Location: ./TPCliente.php");
}
?>  