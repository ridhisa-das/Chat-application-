# Chat-application

## Description

A simple two-user real-time chat application developed using Python socket programming.

## Features

- Client-server communication
- Real-time messaging
- Two-way communication
- Message timestamps
- Two-user chat support
- Client disconnect handling
- Localhost communication

## Technologies Used

- Python
- Socket
- Threading
- Datetime

## Project Files

### server.py
Runs the chat server and manages connected clients.

### client.py
Connects a user to the chat server and allows messages to be sent and received.

## How It Works

1. Start the server.
2. Connect Client 1 to the server.
3. Connect Client 2 to the server.
4. Users can exchange messages in real time.
5. Messages include timestamps.
6. Type `exit` to leave the chat.

## Testing

The application was tested using Google Colab.

Two clients were connected to the same server and successfully exchanged messages.

## Example

Client 1:

Hello from Client 1

Client 2 receives:

[11:15:53] Hello from Client 1

Client 2:

Hello from Client 2

Client 1 receives:

[11:15:53] Hello from Client 2
