<?php

require ("Empleado.php");

$Empleado1 = new Empleado ("Medico", 2000000, "Juan", "Camacho", "Masculino");

echo "Nombre empleado: " . $Empleado1->get_Nombre() . "<br>";
echo "Apellido empleado: " . $Empleado1->get_Apellido() . "<br>";

?>