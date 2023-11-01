<?php

namespace App\Http\Controllers;
use App\Models\Cliente;

use Illuminate\Auth\Events\Validated;
use Illuminate\Http\Request;

class ClienteController extends Controller
{
    public function storeCliente(Request $request)
    {
        $request->validate([
            'nombre' => 'required|min:3',
            'apellido' => 'required|min:3',
            'correo_electronico' => 'required|min:6',
            'telefono' => 'required|min:10' 

        ]);

        $cliente = new Cliente;

        $cliente->nombre = $request->input('nombre');
        $cliente->apellido = $request->input('apellido');
        $cliente->correo_electronico = $request->input('correo_electronico');
        $cliente->telefono = $request->input('telefono');

        try {
            $cliente->save();
            // Si la operación tiene éxito, muestra el mensaje de éxito
            return redirect()->back()->with('success', 'Usuario registrado correctamente');
        } catch (\Exception) {
            // Si hay un error, muestra el mensaje de error
            return redirect()->back()->with('error', 'Hubo un problema al registrar el usuario');
        }
    }
}