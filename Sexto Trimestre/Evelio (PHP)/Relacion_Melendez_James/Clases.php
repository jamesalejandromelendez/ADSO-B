<?php
// 1. Aprendiz
// Atributos del aprendiz: 
// -string idAprendiz, 
// -string nombres, 
// -string apellidos, 
// -string correo
class Aprendiz{
    protected $idAprendiz;
    protected $nombres;
    protected $apellidos;
    protected $correo;
    // public static $contador = 0;

    public function __construct($idAprendiz, $nombres, $apellidos, $correo) {
        $this->idAprendiz = $idAprendiz;
        $this->nombres = $nombres;
        $this->apellidos = $apellidos;
        $this->correo = $correo;
        // Empleado::$contador+=1;
    }
 
    public function verContador(){
        echo '<br>'.'Conteo: ' . self::$contador;
    }
}

// 2. Ficha
// Atributos
// -string codigoFicha, 
// -array aprendices
class Ficha{
    protected $codigoFicha;
    protected $aprendices;
    // public static $contador = 0;

    public function __construct($codigoFicha, $aprendices) {
        $this->codigoFicha = $codigoFicha;
        $this->aprendices = $aprendices;
        // Empleado::$contador+=1;
    }

    public function agregarAprendiz(Aprendiz $aprendiz) {
        $this->aprendices[] = $aprendiz;
    }
 
    public function verContador(){
        echo '<br>'.'Conteo: ' . self::$contador;
    }
}

// 3. Programa
// Atributos:
// -codigoPrograma,
// -nombrePrograma
class Programa{
    protected $codigoPrograma;
    protected $nombrePrograma;
    // public static $contador = 0;

    public function __construct($codigoPrograma, $nombrePrograma) {
        $this->codigoPrograma = $codigoFicha;
        $this->nombrePrograma = $nombrePrograma;
        // Empleado::$contador+=1;
    }
 
    public function verContador(){
        echo '<br>'.'Conteo: ' . self::$contador;
    }
}

?>