<?php
require_once('Clases.php');

// creando instancias

//APRENDIZ
$Aprendiz1 = new Aprendiz('1032677434', 'Alejandro', 'Gómez', 'alejandro@example.com');
$Aprendiz2 = new Aprendiz('52747656', 'Valeria', 'Hernández', 'valeria@gmail.com');
$Aprendiz3 = new Aprendiz('1028466382', 'Roberto', 'Martínez', 'roberto@gmail.com');
$Aprendiz4 = new Aprendiz('1037428463', 'Daniela', 'López', 'daniela@gmail.com');
$Aprendiz5 = new Aprendiz('52878123', 'Carlos', 'Pérez', 'carlos@gmail.com');

$Aprendiz6 = new Aprendiz('123456789', 'Laura', 'Rodríguez', 'laura@example.com');
$Aprendiz7 = new Aprendiz('987654321', 'Mariana', 'Sánchez', 'mariana@gmail.com');
$Aprendiz8 = new Aprendiz('555666777', 'Luis', 'García', 'luis@yahoo.com');
$Aprendiz9 = new Aprendiz('888777666', 'Elena', 'Fernández', 'elena@hotmail.com');
$Aprendiz10 = new Aprendiz('111222333', 'Pedro', 'Díaz', 'pedro@gmail.com');

$Aprendiz11 = new Aprendiz('1032677434','James', 'Smith','James@homatil.com');
$Aprendiz12 = new Aprendiz('52747656', 'Joel', 'Brown', 'Joel@gmail.com');
$Aprendiz13 = new Aprendiz('1028466382', 'Jhon', 'Johnson', 'Jhon@gmail.com');
$Aprendiz14 = new Aprendiz('1037428463', 'Camilo', 'Williams', 'Camilo@gmail.com');
$Aprendiz15 = new Aprendiz('52878123', 'Ana', 'Davis', 'Ana@gmail.com');

// FICHA
$ficha1 = new Ficha('2560664B', []);
$ficha1->agregarAprendiz($Aprendiz1);
$ficha1->agregarAprendiz($Aprendiz2);
$ficha1->agregarAprendiz($Aprendiz3);
$ficha1->agregarAprendiz($Aprendiz4);
$ficha1->agregarAprendiz($Aprendiz5);

$ficha2 = new Ficha('2560664A', []);
$ficha2->agregarAprendiz($Aprendiz6);
$ficha2->agregarAprendiz($Aprendiz7);
$ficha2->agregarAprendiz($Aprendiz8);
$ficha2->agregarAprendiz($Aprendiz9);
$ficha2->agregarAprendiz($Aprendiz10);

$ficha3 = new Ficha('2560665B', []);
$ficha3->agregarAprendiz($Aprendiz11);
$ficha3->agregarAprendiz($Aprendiz12);
$ficha3->agregarAprendiz($Aprendiz13);
$ficha3->agregarAprendiz($Aprendiz14);
$ficha3->agregarAprendiz($Aprendiz15);

// ver listado de las fichas
$aprendicesEnFicha1 = $ficha1->verAprendices();
$aprendicesEnFicha2 = $ficha2->verAprendices();
$aprendicesEnFicha3 = $ficha3->verAprendices();

echo "<h2>Aprendices en la ficha 2560664B:</h2> <br>";
foreach ($aprendicesEnFicha1 as $aprendiz) {
    echo $aprendiz->obtenerNombres() . ' ' . $aprendiz->obtenerApellidos() . '<br>';
}
echo "<h2>Aprendices en la ficha 2560664A:</h2> <br>";
foreach ($aprendicesEnFicha2 as $aprendiz) {
    echo $aprendiz->obtenerNombres() . ' ' . $aprendiz->obtenerApellidos() . '<br>';
}
echo "<h2>Aprendices en la ficha 2560665B:</h2> <br>";
foreach ($aprendicesEnFicha3 as $aprendiz) {
    echo $aprendiz->obtenerNombres() . ' ' . $aprendiz->obtenerApellidos() . '<br>';
}

//PROGRAMA
$progama1 = new Programa('218120', 'ADSO');
?>