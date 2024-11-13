import socket

# Set up the client to listen for broadcasts on port 9999
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(('', 9999))  # Bind to any available IP, listening on port 9999

# Listen for broadcasted messages from Device 1
while True:
    message, addr = client.recvfrom(1024)  # Buffer size is 1024 bytes
    print(f"Received message: {message.decode()} from {addr}")
    
    # Extract server IP from the message
    server_ip = message.decode().split(":")[1].strip()
    print(f"Server is running on IP: {server_ip}")
    
    # Now you can use this IP to connect to Device 1 for chat
    break  # Stop listening after receiving the IP
