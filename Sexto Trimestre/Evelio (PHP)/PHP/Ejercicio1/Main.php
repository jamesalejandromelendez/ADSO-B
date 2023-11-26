<?php

require_once ('./Ahorros.php');
require_once ('./Corriente.php');

//Ahorros
$Ahorros1 = new Ahorros ("1", "04/10/2023", 0.05);
$Ahorros1->Mostar_datos();

//Corriente
$Corriente1 = new Corriente ("1", "04/10/2023");
$Corriente1->Mostar_datos();


?>