<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
    <title>Ocupaciones</title>
</head>
<body>
<div class='container w-25 border p-4 mt-4'>
        <form action="{{route('Ocupaciones')}}" method="POST">
            @csrf
            <h1>Ocupaciones</h1>
            <div class='mb-3'>
                <label for="nombre" class='form-label'>Nombre</label>
                <input type="text" name='nombre' class='form-control' required>
            </div>
                <button type='submit' class='btn btn-primary'>Crear ocupacion</button>
                <a href="{{ route('Profesiones') }}" class='btn btn-primary'>Ir a Profesiones</a>
                <a href="{{ route('Cargos') }}" class='btn btn-primary'>Ir a Cargos</a>
            <div>
            @foreach ($ocupaciones as $ocupacion)
                <p>{{ $ocupacion->nombre }}</p>
            @endforeach
            </div>


        </form>
    </div>
</body>
</html>