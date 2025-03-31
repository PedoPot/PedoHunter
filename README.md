# PedoHunter

## Sequence diagrams of the project workflows
### Send a response to a conversation
```mermaid
sequenceDiagram
    PedoConnector->>PedoController: Received a <br/>new message
    activate PedoController
    PedoController->>DataBase: Save the new message in <br/>the conversation history
    PedoController->>+PedoHunter: Send conversation history
    deactivate PedoController
    PedoHunter-->>-PedoController: Send a response
    activate PedoController
    PedoController->>DataBase: Save the response in <br/>the conversation history
    PedoController-->>PedoConnector: Send the response <br/>to the message
    deactivate PedoController
```

## API usage example

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello, i am Luca"},   
      {"role": "assistant", "content": "I am an AI assistant"},
      {"role": "user", "content": "Who am i?"}               
    ]
  }'
```
```bash
"You are Luca! 😊 \n\nIt's nice to meet you. \n\nDo you want to tell me a little bit about yourself"
```