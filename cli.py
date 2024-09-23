import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Define global variables
client_socket = None

def connect_to_server():
    global client_socket
    server_ip = "127.0.0.1"  # Replace with server IP
    server_port = 9999        # Replace with server port

    try:
        # Create a socket object and connect to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        messagebox.showinfo("Connection Status", "Connected to server.")
        
        # Start a new thread to receive messages from the server
        threading.Thread(target=receive_messages, daemon=True).start()
    except ConnectionRefusedError:
        messagebox.showerror("Connection Error", "Server not running. Please start the server and try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def send_message():
    if client_socket:
        message = message_entry.get()
        if message:
            client_socket.sendall(message.encode())
            message_entry.delete(0, tk.END)
            chat_display.insert(tk.END, f"You: {message}\n")
            chat_display.yview(tk.END)

def receive_messages():
    global client_socket
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                chat_display.insert(tk.END, f"Server: {message}\n")
                chat_display.yview(tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while receiving message: {e}")
            break

# Setup the Tkinter GUI
root = tk.Tk()
root.title("Chat Client")

# Chat display area
chat_display = scrolledtext.ScrolledText(root, state='disabled', width=50, height=20)
chat_display.pack(padx=10, pady=10)

# Message entry field
message_entry = tk.Entry(root, width=40)
message_entry.pack(side=tk.LEFT, padx=(10, 0))

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=10)

# Connect button
connect_button = tk.Button(root, text="Connect to Server", command=connect_to_server)
connect_button.pack(pady=10)

root.mainloop()

