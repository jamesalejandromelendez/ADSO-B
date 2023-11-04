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
    <form action="{{ route('clientes.destroy') }}" method="POST" novalidate>
        <h1>Eliminar</h1>
        @csrf
        @method('DELETE')

        <div class="mb-3">
            <label for="id_cliente" class="form-label">ID del cliente</label>
            <input type="text" name="id_cliente" class="form-control" required>
        </div>

        <button type="submit" class="btn btn-danger">Eliminar</button>
        <a href="{{ route('Registrar') }}" class="btn btn-primary">Crear cliente</a>
    </form>
    </div>
</body>
</html>