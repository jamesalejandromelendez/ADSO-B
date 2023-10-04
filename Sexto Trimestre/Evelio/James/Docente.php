<?php

class Docente {
    private string $nombre;
    private string $Fecha_Nacimiento;
    private string $genero; 
    private string $especialidad;
    
    public function __construct($nombre, $Fecha_Nacimiento, $genero, $especialidad) {
        $this->nombre = $nombre;
        $this->Fecha_Nacimiento = $Fecha_Nacimiento;
        $this->genero = $genero;
        $this->especialidad = $especialidad;
    }

    // GETTERS
    public function getNombre() {
        return $this->nombre;
    }

    public function getFecha_Nacimiento() {
        return $this->Fecha_Nacimiento;
    }

    public function getGenero() {
        return $this->genero;
    }

    public function getEspecialidad() {
        return $this->especialidad;
    }

    // SETTERS
    public function setNombre($nombre) {
        $this->nombre = $nombre;
    }

    public function setFecha_Nacimiento($Fecha_Nacimiento) {
        $this->Fecha_Nacimiento = $Fecha_Nacimiento;
    }

    public function setGenero($genero) {
        $this->genero = $genero;
    }

    public function setEspecialidad($especialidad) {
        $this->especialidad = $especialidad;
    }
}

// instancias

$docente1 = new Docente("Juan Perez", "1990-05-15", "Masculino", "Matemáticas");
$docente2 = new Docente("Ana Rodriguez", "1980-03-20", "Femenino", "Historia");
$docente3 = new Docente("María González", "1983-11-10", "Femenino", "Biología");
$docente4 = new Docente("Carlos Ramirez", "1978-08-25", "Masculino", "Química");
$docente5 = new Docente("Laura Martinez", "1990-12-05", "Femenino", "Inglés");

echo "<h2>Docentes:</h2> ";

echo "Nombre: " . $docente1->getNombre() . ", Fecha de nacimiento: " . $docente1->getFecha_Nacimiento() . ", Género: " . $docente1->getGenero() . ", Especialidad: " . $docente1->getEspecialidad() . "<br>";
echo "Nombre: " . $docente2->getNombre() . ", Fecha de nacimiento: " . $docente2->getFecha_Nacimiento() . ", Género: " . $docente2->getGenero() . ", Especialidad: " . $docente2->getEspecialidad() . "<br>";
echo "Nombre: " . $docente3->getNombre() . ", Fecha de nacimiento: " . $docente3->getFecha_Nacimiento() . ", Género: " . $docente3->getGenero() . ", Especialidad: " . $docente3->getEspecialidad() . "<br>";
echo "Nombre: " . $docente4->getNombre() . ", Fecha de nacimiento: " . $docente4->getFecha_Nacimiento() . ", Género: " . $docente4->getGenero() . ", Especialidad: " . $docente4->getEspecialidad() . "<br>";
echo "Nombre: " . $docente5->getNombre() . ", Fecha de nacimiento: " . $docente5->getFecha_Nacimiento() . ", Género: " . $docente5->getGenero() . ", Especialidad: " . $docente5->getEspecialidad() . "<br>";

?>