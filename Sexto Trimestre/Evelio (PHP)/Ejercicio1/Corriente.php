<?php

require_once('./Cuenta.php');

class Corriente{

    private string $num_chequera;
    private string $fecha_emision_chequera;

    public function __construct(string $num_chequera, string $fecha_emision_chequera)
    {
        $this->num_chequera = $num_chequera;
        $this->fecha_emision_chequera = $fecha_emision_chequera;
    }

    //Metodos GET
    public function get_num_chequera(){
        return $this->num_chequera;
    }

    public function get_fecha_emision_chequera(){
        return $this->fecha_emision_chequera;
    }

    //Metodos SET

    public function set_num_chequera($num_chequera) {
        $this->num_chequera = $num_chequera;
    }

    public function set_fecha_emision_chequera($fecha_emision_chequera) {
        $this->fecha_emision_chequera = $fecha_emision_chequera;
    }

    //Metodo Mostrar datos
    public function Mostar_datos(){
        echo "<br> num_chequera: {$this->num_chequera}, fecha: {$this->fecha_emision_chequera}";
    }
}


?>