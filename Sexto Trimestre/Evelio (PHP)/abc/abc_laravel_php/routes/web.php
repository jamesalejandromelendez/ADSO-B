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
    
    Route::get('/', [ClienteController::class, 'get_ususario'])->name('usuarios');
    Route::get('/home', function () { return view('index'); })->name('Registrar');
    Route::get('/eliminar/{id}', [ClienteController::class, 'mostrarFormularioE'])->name('eliminar');
    Route::get('/editar/{id}', [ClienteController::class, 'mostrarFormularioA'])->name('clientes.editar');
    
    Route::post('/cliente', [ClienteController::class, 'storeCliente'])->name('clientes');
    Route::delete('/eliminar/{id}', [ClienteController::class, 'destroyCliente'])->name('clientes.destroy');
    Route::put('/actualizar/{id}', [ClienteController::class, 'actualizarCliente'])->name('clientes.actualizar');
