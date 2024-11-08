<?php

namespace App\Http\Livewire;

use Livewire\Component;
use Illuminate\Support\Facades\Http;

class Chatbot extends Component
{
    public $userInput;
    public $response;

    public function submit()
    {
        $this->response = "Processing your request...";

        // Simulate calling a serverless API for AI response
        $apiResponse = Http::post('https://your-serverless-api-url.com/inference', [
            'input' => $this->userInput,
        ]);

        $this->response = $apiResponse->json()['response'] ?? 'Error processing your request.';
    }

    public function render()
    {
        return view('livewire.chatbot');
    }
}

