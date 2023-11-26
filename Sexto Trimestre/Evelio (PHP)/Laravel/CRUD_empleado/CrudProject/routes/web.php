<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\EmpleadoController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {return view('welcome');});

Route::get('/Empleado', function () {return view('layouts/Empleado/Empleado');})->name('Registro');
Route::get('/Ver_Empleados', [EmpleadoController::class, 'index'])->name('Empleados');
Route::post('/crear_empleado', [EmpleadoController::class, 'store']);
Route::delete('/eliminar_empleado/{id}', [EmpleadoController::class, 'destroy'])->name('eliminar_empleado');

Route::get('/editar_empleado/{id}', [EmpleadoController::class, 'edit'])->name('editar_empleado');
Route::put('/actualizar_empleado/{id}', [EmpleadoController::class, 'update'])->name('actualizar_empleado');    