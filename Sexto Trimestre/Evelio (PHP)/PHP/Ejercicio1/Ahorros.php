<?php

require_once('./Cuenta.php');

class Ahorros{

    private string $sucursal_apertura;
    private string $fecha_apertura;
    private float $tasa_interes;

    public function __construct(string $sucursal_apertura, string $fecha_apertura, float $tasa_interes)
    {
        $this->sucursal_apertura = $sucursal_apertura;
        $this->fecha_apertura = $fecha_apertura;
        $this->tasa_interes = $tasa_interes;
    }

    //Metodos GET
    public function get_sucursal_apertura(){
        return $this->sucursal_apertura;
    }

    public function get_fecha_apertura(){
        return $this->fecha_apertura;
    }

    public function get_tasa_interes(){
        return $this->tasa_interes;
    }
    //Metodos SET

    public function set_sucursal_apertura($sucursal_apertura) {
        $this->sucursal_apertura = $sucursal_apertura;
    }

    public function set_fecha_apertura($fecha_apertura) {
        $this->fecha_apertura = $fecha_apertura;
    }

    public function set_tasa_interes($tasa_interes) {
        $this->tasa_interes = $tasa_interes;
    }

    //Metodo Mostrar datos
    public function Mostar_datos(){
        echo "<br> Sucursal: {$this->sucursal_apertura}, fecha: {$this->fecha_apertura}, tasa de interes: {$this->tasa_interes}";
    }

}


?>