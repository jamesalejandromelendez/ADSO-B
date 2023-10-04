<?php

require_once 'Docente.php';

class Asignatura {
    private string $nombre;
    private string $creditos;
    private $docente;

    public function __construct($nombre, $creditos, $docente) {
        $this->nombre = $nombre;
        $this->creditos = $creditos;
        $this->docente = $docente;
    }

    // GETTERS
    public function getNombre() {
        return $this->nombre;
    }

    public function getCreditos() {
        return $this->creditos;
    }

    public function getDocente() {
        return $this->docente;
    }

    // SETTERS
    public function setNombre($nombre) {
        $this->nombre = $nombre;
    }

    public function setCreditos($creditos) {
        $this->creditos = $creditos;
    }

    public function setDocente($docente) {
        $this->docente = $docente;
    }
}

// instancias

$asignatura1 = new Asignatura("Matemáticas Avanzadas", 5, $docente1);
$asignatura2 = new Asignatura("Historia Antigua", 4, $docente2);
$asignatura3 = new Asignatura("Biología Celular", 3, $docente3);
$asignatura4 = new Asignatura("Química Orgánica", 4, $docente4);
$asignatura5 = new Asignatura("Inglés Avanzado", 2, $docente5);

echo "<h2>Asignaturas:</h2> ";

echo "Asignatura 1: " . $asignatura1->getNombre() . ", Créditos: " . $asignatura1->getCreditos() . ", Docente: " . $asignatura1->getDocente()->getNombre() . "<br>";
echo "Asignatura 2: " . $asignatura2->getNombre() . ", Créditos: " . $asignatura2->getCreditos() . ", Docente: " . $asignatura2->getDocente()->getNombre() . "<br>";
echo "Asignatura 3: " . $asignatura3->getNombre() . ", Créditos: " . $asignatura3->getCreditos() . ", Docente: " . $asignatura3->getDocente()->getNombre() . "<br>";
echo "Asignatura 4: " . $asignatura4->getNombre() . ", Créditos: " . $asignatura4->getCreditos() . ", Docente: " . $asignatura4->getDocente()->getNombre() . "<br>";
echo "Asignatura 5: " . $asignatura5->getNombre() . ", Créditos: " . $asignatura5->getCreditos() . ", Docente: " . $asignatura5->getDocente()->getNombre() . "<br>";


?>