<?php

class Empleado{
    protected $nombre;
    protected $fechaNacimiento;
    public static $nacionalidad;
    public static $contador = 0; //Contador estático que registra cuantos empleados se crean

    public function __construct($nombre, $fechaNacimiento){
        $this->nombre = $nombre;
        $this->fechaNacimiento=$fechaNacimiento;
        Empleado::$contador+=1; //Cada vez que se genera un objeto se incrementa un contador
    }
    public static function metodoEstatico(){
        echo "Soy un método estático. No necesito un objeto, me invocas desde la clase <br>";
    }
    public function metodoNoEstatico(){
        echo "Soy un método NO estático. Necesito un objeto que me invoque <br>";
    }   
    //Método que procesa un atributo estático verFecha. Note la presencia de la palabra SELF
    // Note tambien la presencia del operador ::
    public function verContador(){
        echo '<br>'.'Conteo: ' . self::$contador;
        return;
    }
    public function verFecha(){
        echo '<br>' . 'Fecha actual: ' . date('d-m-Y');
        return;
    }
}