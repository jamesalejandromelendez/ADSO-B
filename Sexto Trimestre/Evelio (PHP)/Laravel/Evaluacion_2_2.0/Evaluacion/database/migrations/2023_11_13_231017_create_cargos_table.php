<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('cargos', function (Blueprint $table) {
            $table->id('id')->unique();
            $table->unsignedBigInteger('id_ocupacion');
            $table->string('descripcion');
            $table->string('funciones');

            $table->foreign('id_ocupacion')->references('id')->on('ocupacions');
        });
    }
    public $timestamps = false;
    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('cargos');
    }
};
