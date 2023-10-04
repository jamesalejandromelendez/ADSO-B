<?php

class Salon {
    private int $numero;
    private int $capacidad;

    public function __construct($numero, $capacidad) {
        $this->numero = $numero;
        $this->capacidad = $capacidad;
    }

    // GETTERS
    public function getNumero() {
        return $this->numero;
    }

    public function getCapacidad() {
        return $this->capacidad;
    }

    // SETTERS
    public function setNumero($numero) {
        $this->numero = $numero;
    }

    public function setCapacidad($capacidad) {
        $this->capacidad = $capacidad;
    }
}

// instancias

$salon1 = new Salon(101, 30);
$salon2 = new Salon(202, 25);
$salon3 = new Salon(303, 20);
$salon4 = new Salon(404, 35);
$salon5 = new Salon(505, 28);

echo "<h2>Salones:</h2> ";

echo "Número: " . $salon1->getNumero() . ", Capacidad: " . $salon1->getCapacidad() . "<br>";
echo "Número: " . $salon2->getNumero() . ", Capacidad: " . $salon2->getCapacidad() . "<br>";
echo "Número: " . $salon3->getNumero() . ", Capacidad: " . $salon3->getCapacidad() . "<br>";
echo "Número: " . $salon4->getNumero() . ", Capacidad: " . $salon4->getCapacidad() . "<br>";
echo "Número: " . $salon5->getNumero() . ", Capacidad: " . $salon5->getCapacidad() . "<br>";


?>