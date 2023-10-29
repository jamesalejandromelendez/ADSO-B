<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Cliente extends Model
{
    use HasFactory;

    protected $table = 'clientes'; 

    protected $fillable = [
        'nombre',
        'apellido',
        'correo_electronico',
        'telefono',

    ];

    public function reservas()
    {
        return $this->hasMany(Reserva::class);
    }
    // Desactivar marcas de tiempo
    public $timestamps = false; 
}