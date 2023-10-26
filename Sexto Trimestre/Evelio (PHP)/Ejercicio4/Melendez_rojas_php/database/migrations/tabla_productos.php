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
        Schema::create('productos', function (Blueprint $table) {
            $table->id('id_productos');
            $table->string('codigo', 50);
            $table->unsignedBigInteger('id_categoria');
            $table->unsignedBigInteger('id_marca');
            $table->string('descripcion', 50);
            $table->string('unidad_de_medida');
            $table->boolean('disponible');
            $table->decimal('porcentaje_iva', 4, 2);
            $table->decimal('precio_unitario', 20, 2); 
            $table->smallInteger('stock')->unsigned();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('productos');
    }
};