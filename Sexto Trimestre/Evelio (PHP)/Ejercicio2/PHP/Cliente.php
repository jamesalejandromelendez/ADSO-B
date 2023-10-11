<?php

class Personas {

    private string $nombre;
    private string $apellido;
    private string $genero;

    public function __construct(string $nombre, string $apellido, string $genero)
    {
        $this->nombre = $nombre;
        $this->apellido = $apellido;
        $this->genero = $genero;
    }

    //Metodos GET para obtener datos de la persona 
    public function get_Nombre(){
        return $this->nombre;
    }

    public function get_Apellido(){
        return $this->apellido;
    }

    public function get_Genero(){
        return $this->genero;
    }

    //Metodos SET para guardar datos de la persona 

    public function set_Nombre($nombre) {
        $this->nombre = $nombre;
    }

    public function set_Apellido($apellido) {
        $this->apellido = $apellido;
    }

    public function set_Genero($genero) {
        $this->genero = $genero;
    }

}

$persona1 = new Personas ("Juan","Perez","Masculino");



?>