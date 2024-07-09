<?php
namespace App\Services;

use Aws\Lambda\LambdaClient;

class LambdaService
{
    protected $lambdaClient;

    public function __construct()
    {
        $this->lambdaClient = new LambdaClient([
            'version' => 'latest',
            'region'  => config('services.aws.region'),
            'credentials' => [
                'key'    => config('services.aws.credentials.key'),
                'secret' => config('services.aws.credentials.secret')
            ],
        ]);
    }

    public function invokeFunction($functionName, $payload = [])
    {
        $result = $this->lambdaClient->invoke([
            'FunctionName' => $functionName,
            'Payload'      => json_encode($payload),
        ]);

        return json_decode($result->get('Payload')->getContents(), true);
    }
}
