<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ asset('css/Formularios.css') }}">
    <title>Empleados</title>
</head>
<body>

    <form action="{{ url('/crear_empleado') }}" method="post">
        @csrf
        <h2>Registro de Empleado</h2>
        <label for="rol_id">Rol ID:</label>
        <input type="number" id="rol_id" name="rol_id" required><br>

        <label for="home_dress">Dirección de Casa:</label>
        <input type="text" id="home_dress" name="home_dress" required><br>

        <label for="job">Trabajo:</lab el>
        <input type="text" id="job" name="job" required><br>

        <label for="basic_salary">Salario Básico:</label>
        <input type="number" id="basic_salary" name="basic_salary" required><br>

        <label for="admission_date">Fecha de Admisión:</label>
        <input type="date" id="admission_date" name="admission_date" required><br>

        <input type="submit" value="Registrar">
    </form>

    <form action="{{ url('/Ver_Empleados') }}" method="get">
        <button type="submit">Volver</button>
    </form>
</body>
</html>