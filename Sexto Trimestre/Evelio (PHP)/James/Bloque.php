<?php

require_once 'Docente.php';
require_once 'Estudiante.php';
require_once 'Asignatura.php';
require_once 'Salon.php';
require_once 'Bloque.php';

class Bloque {
    private $asignatura;
    private $salon;
    private $numeroBloque;

    public function __construct($asignatura, $salon, $numeroBloque) {
        $this->asignatura = $asignatura;
        $this->salon = $salon;
        $this->numeroBloque = $numeroBloque;
    }

    // GETTERS
    public function getAsignatura() {
        return $this->asignatura;
    }

    public function getSalon() {
        return $this->salon;
    }

    public function getNumeroBloque() {
        return $this->numeroBloque;
    }

    // SETTERS
    public function setAsignatura($asignatura) {
        $this->asignatura = $asignatura;
    }

    public function setSalon($salon) {
        $this->salon = $salon;
    }

    public function setNumeroBloque($numeroBloque) {
        $this->numeroBloque = $numeroBloque;
    }
}

// instancias

$bloque1 = new Bloque($asignatura1, $salon1, 1);
$bloque2 = new Bloque($asignatura2, $salon2, 2);
$bloque3 = new Bloque($asignatura3, $salon3, 3);
$bloque4 = new Bloque($asignatura4, $salon4, 4);
$bloque5 = new Bloque($asignatura5, $salon5, 5);

echo "<h2>Bloques:</h2> ";

echo "Asignatura: " . $bloque1->getAsignatura()->getNombre() . ", Salon: " . $bloque1->getSalon()->getNumero() . ", Número de Bloque: " . $bloque1->getNumeroBloque() . "<br>";
echo "Asignatura: " . $bloque2->getAsignatura()->getNombre() . ", Salon: " . $bloque2->getSalon()->getNumero() . ", Número de Bloque: " . $bloque2->getNumeroBloque() . "<br>";
echo "Asignatura: " . $bloque3->getAsignatura()->getNombre() . ", Salon: " . $bloque3->getSalon()->getNumero() . ", Número de Bloque: " . $bloque3->getNumeroBloque() . "<br>";
echo "Asignatura: " . $bloque4->getAsignatura()->getNombre() . ", Salon: " . $bloque4->getSalon()->getNumero() . ", Número de Bloque: " . $bloque4->getNumeroBloque() . "<br>";
echo "Asignatura: " . $bloque5->getAsignatura()->getNombre() . ", Salon: " . $bloque5->getSalon()->getNumero() . ", Número de Bloque: " . $bloque5->getNumeroBloque() . "<br>";

?>