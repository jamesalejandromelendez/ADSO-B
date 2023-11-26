<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
    <title>Profesiones</title>
</head>
<body>
<div class='container w-25 border p-4 mt-4'>
        <form action="{{route('Profesiones')}}" method="POST">
        @csrf
            <h1>Profesiones</h1>
            <div class='mb-3'>
                <label for="id" class='form-label'>ID</label>
                <input type="text" name='id' class='form-control' >
            </div>
            <div class='mb-3'>
                <label for="nombre" class='form-label'>Nombre</label>
                <input type="text" name='nombre' class='form-control' required>
            </div>
            <div class='mb-3'>
                <label for="titulo" class='form-label'>titulo</label>
                <input type="text" name='titulo' class='form-control' required>
            </div>
                <button type='submit' class='btn btn-primary'>Crear profesion</button>
                    <a href="{{ route('Cargos') }}" class='btn btn-primary'>Ir a Cargos</a>
                    <a href="{{ route('Ocupaciones') }}" class='btn btn-primary'>Ir a Ocupaciones</a>
            <div>
                @foreach ($profesiones as $Profesion)
                    <p>{{ $Profesion->nombre }} {{ $Profesion->titulo }}</p>
                @endforeach
            </div>

        </form>
    </div>
</body>
</html>