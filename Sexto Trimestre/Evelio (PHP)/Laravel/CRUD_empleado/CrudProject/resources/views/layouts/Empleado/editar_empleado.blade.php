<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ asset('css/Formularios.css') }}">
    <title>Actualizar Empleado</title>
</head>
<body>

    <form action="{{ route('actualizar_empleado', $empleado->id) }}" method="post">
        @csrf
        @method('PUT')
        <h2>Actualizar Empleado</h2>

        <label for="rol_id">Rol ID:</label>
        <input type="text" id="rol_id" name="rol_id" value="{{ $empleado->rol_id }}" required><br>

        <label for="home_dress">Dirección de Casa:</label>
        <input type="text" id="home_dress" name="home_dress" value="{{ $empleado->home_dress }}" required><br>

        <label for="job">Trabajo:</label>
        <input type="text" id="job" name="job" value="{{ $empleado->job }}" required><br>

        <label for="basic_salary">Salario Básico:</label>
        <input type="text" id="basic_salary" name="basic_salary" value="{{ $empleado->basic_salary }}" required><br>

        <label for="admission_date">Fecha de Admisión:</label>
        <input type="text" id="admission_date" name="admission_date" value="{{ $empleado->admission_date }}" required><br>

        <input type="submit" value="Actualizar">
    </form>
    <form action="{{ url('/Ver_Empleados') }}" method="get">
        <button type="submit">Volver</button>
    </form>
</body>
</html>