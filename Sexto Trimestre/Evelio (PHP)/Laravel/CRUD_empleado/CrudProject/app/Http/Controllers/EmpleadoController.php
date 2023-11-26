<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Empleado;

class EmpleadoController extends Controller
{
    public function index()
    {
        $empleados = Empleado::all();
        return view('layouts/Empleado/Ver_Empleados', ['empleados' => $empleados]);
    }

    public function store(Request $request)
    {
        $request->validate([
            'rol_id' => 'required|integer',
            'home_dress' => 'required|string',
            'job' => 'required|string',
            'basic_salary' => 'required|numeric',
            'admission_date' => 'required|date',
        ]);

        Empleado::create($request->all());

        return redirect()->route('Empleados')->with('success', 'Empleado registrado exitosamente.');
    }

    public function destroy($id)
    {
        $empleado = Empleado::find($id);

        if ($empleado) {
            $empleado->delete();
            return redirect()->route('Empleados')->with('success', 'Empleado eliminado exitosamente.');
        }

        return redirect()->route('Empleados')->with('error', 'Empleado no encontrado.');
    }

    public function edit($id)
    {
        $empleado = Empleado::findOrFail($id);
        return view('layouts.Empleado.editar_empleado', ['empleado' => $empleado]);
    }

    public function update(Request $request, $id)
    {
        $empleado = Empleado::findOrFail($id);
    
        $request->validate([
            'rol_id' => 'required|integer',
            'home_dress' => 'required|string',
            'job' => 'required|string',
            'basic_salary' => 'required|numeric',
            'admission_date' => 'required|date',
        ]);
    
        $empleado->update($request->all());
    
        return redirect()->route('Empleados')->with('success', 'Empleado actualizado exitosamente.');
    }
};
