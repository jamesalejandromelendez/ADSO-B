<?php

class Cuenta{

    private string $num_cuenta;
    private float $saldo_pesos;
    private float $saldo_dolares;

    public function __construct(string $num_cuenta, float $saldo_pesos, float $saldo_dolares)
    {
        $this->num_cuenta = $num_cuenta;
        $this->saldo_pesos = $saldo_pesos;
        $this->saldo_dolares = $saldo_dolares;
    }

    //Metodos GET
    public function get_Num_cuenta(){
        return $this->num_cuenta;
    }

    public function get_Saldo_pesos(){
        return $this->saldo_pesoslido;
    }

    public function get_Saldo_dolares(){
        return $this->saldo_dolares;
    }
    //Metodos SET

    public function set_Num_cuenta($num_cuenta) {
        $this->num_cuenta = $num_cuenta;
    }

    public function set_Saldo_pesos($saldo_pesos) {
        $this->saldo_pesos = $saldo_pesos;
    }

    public function set_Saldo_dolares($saldo_dolares) {
        $this->saldo_dolares = $saldo_dolares;
    }

    //Metodo Mostrar datos
    public function Mostar_datos(){
        echo "Num_cuenta {$this->num_cuenta} saldo en pesos {$this->saldo_pesos} saldo en dolares {$this->saldo_dolares}";
    }

}

$Cuenta1 = new Cuenta ("1", 2000, 5000);
$Cuenta1->Mostar_datos();


?>