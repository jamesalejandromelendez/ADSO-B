<?php

use App\Http\Controllers\OcupacionesController;
use App\Http\Controllers\CargosController;
use App\Http\Controllers\ProfesionesController;
use Illuminate\Support\Facades\Route;

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

Route::get('/', function () {
    return view('welcome');
});
/*----------------------------------------------------------------------------------------*/

Route::get('/ocupaciones', function () {
    return view('layout/Ocupaciones');})->name('Ocupaciones');

Route::get('/ocupaciones', [OcupacionesController::class, 'index'])->name('Ocupaciones');

Route::post('/ocupaciones', [OcupacionesController::class, 'store'])->name('Ocupaciones');

/*----------------------------------------------------------------------------------------*/

Route::get('/profesiones', function () {
    return view('layout/Profesiones');})->name('Profesiones');

Route::get('/profesiones', [ProfesionesController::class, 'index'])->name('Profesiones');

Route::post('/profesiones', [ProfesionesController::class, 'store'])->name('Profesiones');

/*----------------------------------------------------------------------------------------*/

Route::get('/cargos', function () {
    return view('layout/Cargos');})->name('Cargos');

Route::get('/cargos', [CargosController::class, 'index'])->name('Cargos');

Route::post('/cargos', [CargosController::class, 'store'])->name('Cargos');

