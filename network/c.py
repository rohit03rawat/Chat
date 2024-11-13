import socket
import time

# Port to listen for the server's broadcast
PORT = 12345

# Create a socket to listen for broadcast messages
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.bind(('', PORT))

# Function to start chatting with the server
def start_chat(server_ip):
    try:
        # Connect to the server
        print(f"Connecting to server at {server_ip}:{PORT}...")
        chat_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        chat_socket.connect((server_ip, PORT))
        print("Connected to server.")

        # Start sending and receiving messages
        while True:
            message = input("Enter message to send: ")
            if message.lower() == 'exit':
                print("Closing connection...")
                break
            chat_socket.sendall(message.encode())
            server_message = chat_socket.recv(1024).decode()
            print(f"Server says: {server_message}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        chat_socket.close()

# Listen for incoming broadcast IPs
def listen_for_ip():
    while True:
        try:
            message, addr = client_socket.recvfrom(1024)
            server_ip = message.decode()
            print(f"Received broadcast from {addr}: {server_ip}")

            # Start the chat with the received IP address
            start_chat(server_ip)
            break  # Exit after starting chat
        except Exception as e:
            print(f"Error receiving broadcast: {e}")

# Start listening for the IP and connecting to the server
listen_for_ip()
