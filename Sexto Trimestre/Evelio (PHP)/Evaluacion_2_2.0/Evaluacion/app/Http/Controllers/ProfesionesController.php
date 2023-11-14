<?php

namespace App\Http\Controllers;
use App\Models\Profesiones;
use Illuminate\Http\Request;

class ProfesionesController extends Controller
{
    public function index()
    {
        $profesiones = Profesiones::all();
        return view('layout.Profesiones', ['profesiones' => $profesiones]);
    }

    public function store (request $request){
        $request->validate([
            'nombre' => 'required|min:1',
            'titulo' => 'required|min:1'
        ]);

        $Profesiones = new Profesiones;
        $Profesiones->nombre = $request->nombre;
        $Profesiones->titulo = $request->titulo;
        $Profesiones->save();

        return redirect()->route('Profesiones')->with('success', 'Profesiones creada Correctamente');

     }
}

