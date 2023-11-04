<?php

use App\Http\Controllers\ClienteController;
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

Route::get('/', [ClienteController::class, 'get_ususario'])->name('ususarios');

Route::get('/home', function () {return view('index');})->name('Registrar');

Route::get('/eliminar', function () {return view('Eliminar_usuario');})->name('eliminar');

Route::post('/cliente', [ClienteController::class, 'storeCliente'])->name('clientes');

Route::delete('/eliminar', [ClienteController::class, 'destroyCliente'])->name('clientes.destroy');


