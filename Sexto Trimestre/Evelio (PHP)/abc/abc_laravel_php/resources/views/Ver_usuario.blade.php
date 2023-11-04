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
        @foreach($clientes as $cliente) 

        <p class='clientes'>{{ $cliente->nombre }} {{ $cliente->apellido }} - {{ $cliente->correo_electronico }} - {{ $cliente->telefono }}</p>

        @endforeach
        <a href="{{ route('eliminar') }}" class='btn btn-danger'>Eliminar usuario</a>
        <a href="{{ route('Registrar') }}" class='btn btn-primary'>Crear usuario</a>
    </div>
</body>
</html>