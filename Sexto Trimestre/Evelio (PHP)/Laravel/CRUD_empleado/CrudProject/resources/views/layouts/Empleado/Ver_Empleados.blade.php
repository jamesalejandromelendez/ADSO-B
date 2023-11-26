<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ asset('css/Ver_Empleados.css') }}">
    <title>Lista de Empleados</title>
</head>
<body>
<h2>Lista de Empleados</h2>

<form action="{{ url('/Empleado') }}" method="get">
    <button type="submit">Registrar Empleado</button>
</form>

    @if($empleados !== null && count($empleados) > 0)
        <table>
            <thead>
                <tr>
                    <th>Rol ID</th>
                    <th>Dirección de Casa</th>
                    <th>Trabajo</th>
                    <th>Salario Básico</th>
                    <th>Fecha de Admisión</th>
                </tr>
            </thead>
            <tbody>
                @foreach($empleados as $empleado)
                    <tr>
                        <td>{{ $empleado->rol_id }}</td>
                        <td>{{ $empleado->home_dress }}</td>
                        <td>{{ $empleado->job }}</td>
                        <td>{{ $empleado->basic_salary }}</td>
                        <td>{{ $empleado->admission_date }}</td>
                        <td class="button-container">
                            <a href="{{ route('editar_empleado', $empleado->id) }}" class="update-button">Actualizar</a>
                            <form action="{{ route('eliminar_empleado', $empleado->id) }}" method="post" onsubmit="return confirm('¿Estás seguro de eliminar este empleado?')">
                                @csrf
                                @method('DELETE')
                                <button type="submit" class="delete-button">Eliminar</button>
                            </form>
                        </td>
                    </tr>
                @endforeach
            </tbody>
        </table>
    @else
        <p>No hay empleados registrados.</p>
    @endif

</body>
</html>