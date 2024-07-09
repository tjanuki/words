<?php

namespace App\Service;

use Illuminate\Support\Facades\Http;

class OpenAIChatService
{

    private string $baseUrl = 'https://api.openai.com/v1/chat/completions';

    public function __construct(private string $apiKey, private string $model)
    {
    }

    public function sendMessage(array $messages)
    {
        $response = Http::withHeaders([
            'Content-Type' => 'application/json',
            'Authorization' => 'Bearer ' . $this->apiKey,
        ])->post($this->baseUrl, [
            'model' => $this->model,
            'messages' => $messages
        ]);

        return $response->json();
    }
}
