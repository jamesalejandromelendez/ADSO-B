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
            return redirect('/')->with('success', 'Usuario registrado correctamente');
        } catch (\Exception) {
            return redirect()->back()->with('error', 'Hubo un problema al registrar el usuario');
        }
    }

    public function get_ususario()
    {
        $clientes = Cliente::all();
        return view('Ver_usuario', ['clientes' => $clientes]);
    }
    
    public function destroyCliente(Request $request)
    {
        $request->validate([
            'id_cliente' => 'required|min:1',
        ]);
    
        $id = $request->input('id_cliente');
    
        try {
            $cliente = Cliente::findOrFail($id);
            $cliente->delete();

            return redirect()->route('ususarios')->with('success', 'Cliente eliminado correctamente');
        } catch (\Exception $e) {
            return redirect()->route('eliminar')->with('error', 'Hubo un problema al eliminar el cliente');
        }
    }
    
}