<?php

namespace App\Http\Controllers;
use App\Models\Cliente; // Asegúrate de importar el modelo Cliente

use Illuminate\Auth\Events\Validated;
use Illuminate\Http\Request;

class HoteleriaController extends Controller
{
    public function storeCliente(Request $request)
    {
        $request->validate([
            'nombre' => 'required|min:3'
        ]);

        $cliente = new Cliente;

        // Asignar valores desde la solicitud (si es necesario)
        $cliente->nombre = $request->input('nombre');
        $cliente->nombre = $request->input('apellido');
        $cliente->nombre = $request->input('email');
        $cliente->nombre = $request->input('telefono');
        $cliente->save();

        return redirect()->route('index')->with('success', 'usuario registrado correctamente');
    }
}