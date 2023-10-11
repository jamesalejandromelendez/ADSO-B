<?php

require_once 'Asignatura.php';
require_once 'Salon.php';

class Curso {
    private  $asignatura;
    private  $salon;
    private string $horario;

    public function __construct($asignatura, $salon, $horario) {
        $this->asignatura = $asignatura;
        $this->salon = $salon;
        $this->horario = $horario;
    }

    // GETTERS
    public function getAsignatura() {
        return $this->asignatura;
    }

    public function getSalon() {
        return $this->salon;
    }

    public function getHorario() {
        return $this->horario;
    }

    // SETTERS
    public function setAsignatura($asignatura) {
        $this->asignatura = $asignatura;
    }

    public function setSalon($salon) {
        $this->salon = $salon;
    }

    public function setHorario($horario) {
        $this->horario = $horario;
    }
}

$curso1 = new Curso($asignatura1, $salon1, "Lunes 08:00 - 10:00");
$curso2 = new Curso($asignatura2, $salon2, "Martes 10:30 - 12:30");
$curso3 = new Curso($asignatura3, $salon3, "Miércoles 13:00 - 15:00");
$curso4 = new Curso($asignatura4, $salon4, "Jueves 15:30 - 17:30");
$curso5 = new Curso($asignatura5, $salon5, "Viernes 18:00 - 20:00");

echo "<h2>Cursos:</h2> ";

echo "Curso 1: " . $curso1->getAsignatura()->getNombre() . ", Salon: " . $curso1->getSalon()->getNumero() . ", Horario: " . $curso1->getHorario() . "<br>";
echo "Curso 2: " . $curso2->getAsignatura()->getNombre() . ", Salon: " . $curso2->getSalon()->getNumero() . ", Horario: " . $curso2->getHorario() . "<br>";
echo "Curso 3: " . $curso3->getAsignatura()->getNombre() . ", Salon: " . $curso3->getSalon()->getNumero() . ", Horario: " . $curso3->getHorario() . "<br>";
echo "Curso 4: " . $curso4->getAsignatura()->getNombre() . ", Salon: " . $curso4->getSalon()->getNumero() . ", Horario: " . $curso4->getHorario() . "<br>";
echo "Curso 5: " . $curso5->getAsignatura()->getNombre() . ", Salon: " . $curso5->getSalon()->getNumero() . ", Horario: " . $curso5->getHorario() . "<br>";

?>