<?php

namespace App\Providers;

use App\Service\OpenAIChatService;
use Illuminate\Support\ServiceProvider;

class AppServiceProvider extends ServiceProvider
{
    /**
     * Register any application services.
     */
    public function register(): void
    {
        $this->app->singleton(OpenAIChatService::class, function ($app) {
            $apiKey = config('services.openai.api_key');
            $model = config('services.openai.model');

            return $app->make(OpenAIChatService::class, [
                'apiKey' => $apiKey,
                'model' => $model,
            ]);
        });
    }

    /**
     * Bootstrap any application services.
     */
    public function boot(): void
    {
        //
    }
}
