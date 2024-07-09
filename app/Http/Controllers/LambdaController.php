<?php

namespace App\Http\Controllers;

use App\Services\LambdaService;
use Illuminate\Http\Request;

class LambdaController extends Controller
{
    public function __construct(private readonly LambdaService $lambdaService)
    {
    }

    public function __invoke(Request $request)
    {
        $functionName = 'python-lambda-sandbox-dev-basicFunction';
        $payload = [];

        $result = $this->lambdaService->invokeFunction($functionName, $payload);

        return response()->json($result);
    }
}
