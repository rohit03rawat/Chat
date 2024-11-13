import socket
import threading

# Function to handle communication with a client
def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            broadcast(message, client_socket, clients)
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

# Function to broadcast messages to all connected clients
def broadcast(message, current_client, clients):
    for client in clients:
        if client != current_client:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

# Main server function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9999))  # Bind to localhost and port 9999
    server.listen(5)  # Listen for incoming connections
    print("Server started on port 9999...")

    clients = []

    while True:
        client_socket, addr = server.accept()
        print(f"Client {addr} connected")
        clients.append(client_socket)

        # Start a new thread to handle the connected client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, clients))
        client_thread.start()

if __name__ == "__main__":
    main()
