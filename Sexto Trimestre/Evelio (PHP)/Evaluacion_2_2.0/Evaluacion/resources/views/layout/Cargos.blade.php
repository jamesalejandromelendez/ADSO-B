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
        <form action="{{route('Cargos')}}" method="POST">
        @csrf
            <h1>Cargos</h1>
            <div class='mb-3'>
                <label for="id_ocupacion" class='form-label'>ID_ocupacion</label>
                <input type="text" name='id_ocupacion' class='form-control' required>
            </div>
            <div class='mb-3'>
                <label for="descripcion" class='form-label'>Descripcion</label>
                <input type="text" name='descripcion' class='form-control' required>
            </div>
            <div class='mb-3'>
                <label for="funciones" class='form-label'>Funciones</label>
                <input type="text" name='funciones' class='form-control' required>
            </div>
                <button type='submit' class='btn btn-primary'>Crear Cargo</button>
                <a href="{{ route('Profesiones') }}" class='btn btn-primary'>Ir a Profesiones</a>
                <a href="{{ route('Ocupaciones') }}" class='btn btn-primary'>Ir a Ocupaciones</a>
                @foreach ($cargos as $cargo)
                    <p>{{ $cargo->id_ocupacion }} {{ $cargo->descripcion }} {{ $cargo->funciones}}</p>
                @endforeach
        </form>
    </div>
</body>
</html>