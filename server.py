
import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 12345

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(2)

print("====================================")
print("          CHAT SERVER")
print("====================================")
print("Server started...")
print("Waiting for users...")

def get_time():
    return datetime.now().strftime("%H:%M:%S")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                if client in clients:
                    clients.remove(client)

def handle_client(client, address):
    print("User connected:", address)

    client.send("Connected to the chat server.".encode())

    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            formatted_message = "[" + get_time() + "] " + message

            print(formatted_message)
            broadcast(formatted_message, client)

        except:
            break

    if client in clients:
        clients.remove(client)

    client.close()
    print("User disconnected:", address)

while True:
    client, address = server.accept()

    if len(clients) >= 2:
        client.send("Chat room is full.".encode())
        client.close()
        continue

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client, address)
    )

    thread.start()
