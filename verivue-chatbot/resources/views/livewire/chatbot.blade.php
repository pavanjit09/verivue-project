<div>
    <h3>Ask VeriVue Chatbot</h3>
    <input type="text" wire:model="userInput" placeholder="Type your question...">
    <button wire:click="submit">Submit</button>
    <p><strong>Response:</strong> {{ $response }}</p>
</div>

