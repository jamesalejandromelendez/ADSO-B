<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;
use App\Models\Cliente;

class CrearUsuario extends Command
{
    protected $signature = 'usuario:crear';

    protected $description = 'Crea un nuevo usuario';

    public function handle()
    {
        $nombre = $this->ask('Ingrese el nombre del usuario:');
        $apellido = $this->ask('Ingrese el apellido del usuario:');
        $correo_electronico = $this->ask('Ingrese el correo electrónico del usuario:');
        $telefono = $this->ask('Ingrese el teléfono del usuario:');

        Cliente::create([
            'nombre' => $nombre,
            'apellido' => $apellido,
            'correo_electronico' => $correo_electronico,
            'telefono' => $telefono,
        ]);

        $this->info('Usuario creado correctamente.');
    }
}
