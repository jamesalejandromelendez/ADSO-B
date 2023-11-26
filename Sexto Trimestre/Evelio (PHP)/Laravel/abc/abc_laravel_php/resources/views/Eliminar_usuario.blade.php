<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
    <title>Eliminar Usuario</title>
</head>
<body>
    <div class='container w-25 border p-4 mt-4'>
        <form action="{{ route('clientes.destroy', ['id' => $cliente->id]) }}" method="POST">
            @csrf
            @method('DELETE')
            
            @if(Session::has('error'))
                <div class="alert alert-danger flash-message">
                    {{ Session::get('error') }}
                </div>
            @endif

            <h1>Eliminar</h1>

            <div class="mb-3">
                <label for="id_cliente" class="form-label">ID del cliente</label>
                <span class="form-control">{{ $cliente->id }}</span>
            </div>

            <div class='mb-3'>
                <label for="nombre" class='form-label'>Nombre</label>
                <span class='form-control'>{{ $cliente->nombre }}</span>
            </div>

            <div class='mb-3'>
                <label for="apellido" class='form-label'>Apellido</label>
                <span class='form-control'>{{ $cliente->apellido }}</span>
            </div>

            <button type="submit" class="btn btn-danger">Eliminar</button>
            <a href="{{ route('Registrar') }}" class="btn btn-primary">Crear cliente</a>
            <a href="{{ route('usuarios') }}" class='btn btn-update'>usuarios</a>
        </form>
    </div>
</body>
</html>