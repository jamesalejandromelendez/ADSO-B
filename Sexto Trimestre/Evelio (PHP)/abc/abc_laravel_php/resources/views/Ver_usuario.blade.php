<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
    <title>Usuarios</title>
</head>
<body>
    <div class='container w-25 border p-4 mt-4'>
        <h1>Usuarios</h1>

        @foreach ($clientes as $cliente)
            <p>{{ $cliente->nombre }} {{ $cliente->apellido }} - 
                <a href="{{ route('clientes.editar', ['id' => $cliente->id]) }}" class='editar'>Editar</a> - <a href="{{ route('eliminar', ['id' => $cliente->id]) }}" class='eliminar'>Eliminar</a>
            </p>
        @endforeach

        <a href="{{ route('Registrar') }}" class='btn btn-primary'>Crear</a>

    </div>
</body>
</html>