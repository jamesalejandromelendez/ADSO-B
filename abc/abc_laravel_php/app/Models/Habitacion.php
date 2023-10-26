<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Habitacion extends Model
{
    use HasFactory;

    protected $table = 'habitaciones';

    protected $fillable = [
        'tipo_habitacion',
        'estado',
        'id_reserva',

    ];
    
    public function reserva()
    {
        return $this->belongsTo(Reserva::class, 'id_reserva');
    }
}