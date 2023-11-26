<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
    <title>Registrar Usuario</title>
</head>
<body>
    <div class='container w-25 border p-4 mt-4'>
        <form action='{{ route("clientes") }}' method='POST' novalidate>
            @csrf
            @if(Session::has('success'))
                <div class="alert alert-success">
                    {{ Session::get('success') }}
                </div>
            @endif

            @if(Session::has('error'))
                <div class="alert alert-danger flash-message">
                    {{ Session::get('error') }}
                </div>
            @endif

            <h1>Registrarse</h1>
            <div class='mb-3'>
                <label for="nombre" class='form-label'>Nombre</label>
                <input type="text" name='nombre' class='form-control'>
            </div>
            <div class='mb-3'>
                <label for="apellido" class='form-label'>Apellido</label>
                <input type="text" name='apellido' class='form-control' required>
            </div>

            <div class='mb-3'>
                <label for="correo_electronico" class='form-label'>Correo Electrónico</label>
                <input type="email" name='correo_electronico' class='form-control' required>
            </div>

            <div class='mb-3'>
                <label for="telefono" class='form-label'>Teléfono</label>
                <input type="text" name='telefono' class='form-control' required>
            </div>
                <button type='submit' class='btn btn-primary'>Crear usuario</button>
                <a href="{{ route('usuarios') }}" class='btn btn-update'>usuarios</a>
        </form>

    </div>
</body>
</html>

