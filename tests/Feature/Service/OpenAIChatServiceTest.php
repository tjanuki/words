<?php

use App\Service\OpenAIChatService;

beforeEach(function () {
    $this->chatService = app(OpenAIChatService::class);
});

it('returns a chat reply', function () {
    $messages = [
        ["role" => "system", "content" => "You are a helpful assistant."],
        ["role" => "user", "content" => "Who won the world series in 2020?"],
        ["role" => "assistant", "content" => "The Los Angeles Dodgers won the World Series in 2020."],
        ["role" => "user", "content" => "Where was it played?"]
    ];

    $response = $this->chatService->sendMessage($messages);

    // prettier-ignore
    expect($response)->toHaveKeys(['choices'])
        ->and($response['choices'])->toBeArray()
        ->and($response['choices'][0])->toHaveKeys(['message', 'index'])
        ->and($response['choices'][0]['message'])->toHaveKeys(['role', 'content'])
        ->and($response['choices'][0]['message']['role'])->toBe('assistant')
        ->and($response['choices'][0]['message']['content'])->toContain('Globe Life Field');
});
