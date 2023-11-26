<?php

require ('./persona.php');
//Empleado deriva de persona

class Empleado extends Personas {
    private string $cargo;
    private float $salario;

    public function __construct(string $cargo, float $salario, string $nombre, string $apellido, string $genero){
        //Llamar al constructor de la super clase persona 
        parent::__construct($nombre, $apellido, $genero);
        //Definir los atributos que se cargan a la subclase Empleado 
        $this->cargo = $cargo;
        $this->salario = $salario;
    }

    public function get_Cargo(){
        return $this->cargo;
    }

    public function get_Salario(){
        return $this->salario;
    }

    
    public function set_Cargo($nombre){
        $this->cargo=$cargo;
    }

    public function set_Salario($salario){
        $this->salario=$salario;
    }
}

$Empleado1 = new Empleado ("Medico", 2000000, "Juan", "Camacho", "Masculino");

echo "<br> Cargo del empleado: " . $Empleado1->get_Cargo() . "<br>";

?>