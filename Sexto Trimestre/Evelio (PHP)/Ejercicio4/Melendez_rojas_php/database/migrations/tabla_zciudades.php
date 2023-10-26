<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('ciudades', function (Blueprint $table) {
            $table->id('id_ciudad')->unsigned();
            $table->string('codigo_pais');
            $table->string('nombre', 50);

            // Agregamos la clave foránea correctamente
            $table->foreign('codigo_pais')->references('codigo_pais')->on('paises');
        });
    }

    
    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('ciudades');
    }
};