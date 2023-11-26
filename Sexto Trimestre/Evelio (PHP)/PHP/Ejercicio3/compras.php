<?php

//Clase Producto
//+++++++++++++++++++++++++++++++++++++++++++++
class Producto {
    private $nombreProducto;
    private $precio;

    public function __construct(
        $nombreProducto,
        $precio) {
    
        $this->nombreProducto = $nombreProducto;
        $this->precio = $precio;
    }
    //Métodos GET's
    public function getNombreProducto() {
        return $this->nombreProducto;
    }
    public function getPrecio() {
        return $this->precio;
    }
}

// Clase Carro de compras
//********************************************* */
class CarroCompra {
    private $productos = array();

    //Métodos del carro de compra. 
    public function agregarProducto(Producto $producto) {
        $this->productos[] = $producto;
    }
    public function getSubtotal() {
        $subtotal = 0;
        foreach ($this->productos as $producto) {
            $subtotal += $producto->getPrecio();
        }
        return $subtotal;
    }
    public function vaciarCarro() {
        $this->productos = array();
    }
}
//+++++++++++++++++++++++++++++++++++++++++++++++++++
//Una clase Pedido que guarda los datos de un pedido de productos
class Pedido {
    private $nombreCliente;
    private $correoCliente;
    private $direccionCliente;
    private $carro;

    //Método constructor del pedido con el nombre, correo dirección del cliente y un objeto carro
    public function __construct(
        $nombreCliente,
        $correoCliente,
        $direccionCliente,
        CarroCompra $carro)
        {
        $this->nombreCliente = $nombreCliente;
        $this->correoCliente = $correoCliente;
        $this->direccionCliente = $direccionCliente;
        $this->carro = $carro;
    }
    public function getTotal() {
        return $this->carro->getSubtotal();
    }
    public function procesarPedido() {
        // Conectar a la base de datos y guardar el pedido
        // Enviar un correo electrónico de confirmación al cliente
        // Actualizar el inventario de productos en la tienda
        $this->carro->vaciarCarro();
        return true;
    }
}

// Ejemplo de uso
$producto1 = new Producto("Camiseta", 80);
$producto2 = new Producto("Pantalón", 120);
$producto3 = new Producto("Tennis", 250);
$producto4 = new Producto("Calcetines", 12);
$producto5 = new Producto("Boxer", 20);

$carro1 = new CarroCompra();
$carro1->agregarProducto($producto1);
$carro1->agregarProducto($producto2);
$carro1->agregarProducto($producto4);

$pedido1 = new Pedido("Juan Pérez", "juanperez@example.com", "Calle 123", $carro1);

echo "Total del pedido: $" . $pedido1->getTotal() . "<br>";

if ($pedido1->procesarPedido()) {
    echo "Gracias por su compra";
} else {
    echo "Ha ocurrido un error, por favor inténtelo de nuevo";
}
?>
