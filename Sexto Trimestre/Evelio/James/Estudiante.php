<?php

class Estudiante {
    private string $nombre;
    private int $edad;
    private string $grado;

    public function __construct($nombre, $edad, $grado) {
        $this->nombre = $nombre;
        $this->edad = $edad;
        $this->grado = $grado;
    }

    // GETTERS
    public function getNombre() {
        return $this->nombre;
    }

    public function getEdad() {
        return $this->edad;
    }

    public function getGrado() {
        return $this->grado;
    }

    // SETTERS
    public function setNombre($nombre) {
        $this->nombre = $nombre;
    }

    public function setEdad($edad) {
        $this->edad = $edad;
    }

    public function setGrado($grado) {
        $this->grado = $grado;
    }
}

// instancias

$estudiante1 = new Estudiante("Carlos Gomez", 18, "12°");
$estudiante2 = new Estudiante("Laura Diaz", 17, "11°");
$estudiante3 = new Estudiante("Luis Hernandez", 16, "10°");
$estudiante4 = new Estudiante("Ana Silva", 17, "11°");
$estudiante5 = new Estudiante("Pedro Martinez", 18, "12°");

echo "<h2>Estudiantes:</h2> ";

echo "Nombre: " . $estudiante1->getNombre() . ", Edad: " . $estudiante1->getEdad() . ", Grado: " . $estudiante1->getGrado() . "<br>";
echo "Nombre: " . $estudiante2->getNombre() . ", Edad: " . $estudiante2->getEdad() . ", Grado: " . $estudiante2->getGrado() . "<br>";
echo "Nombre: " . $estudiante3->getNombre() . ", Edad: " . $estudiante3->getEdad() . ", Grado: " . $estudiante3->getGrado() . "<br>";
echo "Nombre: " . $estudiante4->getNombre() . ", Edad: " . $estudiante4->getEdad() . ", Grado: " . $estudiante4->getGrado() . "<br>";
echo "Nombre: " . $estudiante5->getNombre() . ", Edad: " . $estudiante5->getEdad() . ", Grado: " . $estudiante5->getGrado() . "<br>";

?>