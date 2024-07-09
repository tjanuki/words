<?php

use App\Services\LambdaService;

it('invokes a lambda function', function () {
    $lambdaService = app(LambdaService::class);
    $response = $lambdaService->invokeFunction('python-lambda-sandbox-dev-basicFunction');

    // prettier-ignore
    expect($response)->toBeArray()
        ->and($response)->toHaveKey('statusCode')
        ->and($response['statusCode'])->toBe(200)
        ->and($response)->toHaveKey('body')
        ->and($response['body'])->toBe('{"message": "Hello from basic_function!", "event": []}');
});

