
import socket
import threading

HOST = "127.0.0.1"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("====================================")
print("           CHAT CLIENT")
print("====================================")
print("Connected to the chat server.")
print("Type your message.")
print("Type 'exit' to leave the chat.")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                print("Server disconnected.")
                break

            print("\n" + message)

        except:
            break

thread = threading.Thread(
    target=receive_messages,
    daemon=True
)

thread.start()

while True:
    try:
        message = input("You: ")

        if message.lower() == "exit":
            print("Disconnected from chat.")
            client.close()
            break

        if message.strip():
            client.send(message.encode())

    except:
        client.close()
        break
