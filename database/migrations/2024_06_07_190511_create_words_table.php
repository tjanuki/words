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
        Schema::create('words', function (Blueprint $table) {
            $table->id();
            $table->string('term');
            $table->string('definition');
            $table->string('lexical_category')->nullable();
            $table->json('examples')->nullable();
            $table->boolean('is_loading')->default(false);
            $table->integer('times')->default(1);
            $table->float('easiness_factor')->default(2.5);
            $table->integer('repetition_number')->default(0);
            $table->integer('interval')->default(1);

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('words');
    }
};
