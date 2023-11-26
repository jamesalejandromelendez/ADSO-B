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
    public function mostrarFormularioE($id_cliente)
    {
        $cliente = Cliente::findOrFail($id_cliente);
        return view('Eliminar_usuario', ['cliente' => $cliente]);
    }
    
    public function destroyCliente($id_cliente)
    {
        try {
            $cliente = Cliente::findOrFail($id_cliente);
            $cliente->delete();
            return redirect()->route('usuarios')->with('success', 'Usuario eliminado correctamente');

        } catch (\Exception $e) {
            return redirect()->route('eliminar', ['id' => $id_cliente])->with('error', 'Hubo un problema ');
        }
    }

    public function mostrarFormularioA($id_cliente)
    {
        $cliente = Cliente::findOrFail($id_cliente);
        return view('Actualizar_usuario', ['cliente' => $cliente]);
    }

    public function actualizarCliente(Request $request, $id_cliente)
    {
        $request->validate([
            'nombre' => 'required|min:3',
            'apellido' => 'required|min:3',
            'correo_electronico' => 'required|min:6',
            'telefono' => 'required|min:10',
        ]);

        $cliente = Cliente::findOrFail($id_cliente);

        $cliente->nombre = $request->input('nombre');
        $cliente->apellido = $request->input('apellido');
        $cliente->correo_electronico = $request->input('correo_electronico');
        $cliente->telefono = $request->input('telefono');

        try {
            $cliente->save();
            return redirect()->route('ususarios')->with('success', 'Cliente actualizado correctamente');
            
        } catch (\Exception $e) {
            return redirect()->route('usuarios', ['id_cliente' => $id_cliente])->with('error', 'Hubo un problema al actualizar el cliente');
        }
    }
}