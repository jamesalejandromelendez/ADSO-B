<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Ejecuta las migraciones.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('seguimiento_productos', function (Blueprint $table) {
            $table->id('id_seguimiento')->unsigned();
            $table->string('usuario', 50);
            $table->dateTime('fecha');
        });
    }

    /**
     * Deshace las migraciones.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('seguimiento_productos');
    }
};