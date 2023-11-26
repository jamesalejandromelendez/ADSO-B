<?php

namespace App\Http\Controllers;
use Illuminate\Http\Request;
use App\Models\Ocupacion;

class OcupacionesController extends Controller
{
    public function index()
    {
        $ocupaciones = Ocupacion::all();
        return view('layout.Ocupaciones', ['ocupaciones' => $ocupaciones]);
    }

     public function store (request $request){
        $request->validate([
            'nombre' => 'required|min:3'
        ]);

        $Ocupacion = new Ocupacion;
        $Ocupacion->nombre = $request->nombre;
        $Ocupacion->save();

        return redirect()->route('Ocupaciones')->with('success', 'Ocupacion creada Correctamente');

     }
}
