<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\Cargos;

class CargosController extends Controller
{
    public function index()
    {
        $cargos = Cargos::all();
        return view('layout.Cargos', ['cargos' => $cargos]);
    }

    public function store (request $request){
        $request->validate([
            'id_ocupacion' => 'required|min:1',
            'descripcion' => 'required|min:1',
            'funciones' => 'required|min:1'
        ]);

        $Cargos = new Cargos;
        $Cargos->id_ocupacion = $request->id_ocupacion;
        $Cargos->descripcion = $request->descripcion;
        $Cargos->funciones = $request->funciones;
        $Cargos->save();

        return redirect()->route('Cargos')->with('success', 'Cargos creada Correctamente');

     }
}
