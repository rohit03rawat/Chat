import socket
import time

def get_local_ip():
    # Try to connect to an external server (Google DNS) to get the actual IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # Connect to an external server to find the local IP
        s.connect(('8.8.8.8', 80))  # Google's public DNS
        ip = s.getsockname()[0]  # Get the local IP address used to reach the external server
    except Exception:
        ip = '127.0.0.1'  # Default to localhost if there's an error
    finally:
        s.close()
    return ip

# Get the actual local IP address of the device
SERVER_IP = get_local_ip()
PORT = 12345

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_IP, PORT))
server.listen()

print(f"Server running on {SERVER_IP}:{PORT}")

# Broadcasting server's IP address over UDP to the network
broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
broadcast_socket.settimeout(2)  # Timeout after 2 seconds

# Broadcast the IP address every 5 seconds
while True:
    message = f"Server IP: {SERVER_IP}"
    broadcast_socket.sendto(message.encode(), ('<broadcast>', 9999))
    print(f"Broadcasting IP: {SERVER_IP}")
    time.sleep(5)  # Wait for 5 seconds before sending the next broadcast
