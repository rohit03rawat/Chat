import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Function to receive messages from the server
def receive_messages(client_socket, text_area):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            text_area.config(state=tk.NORMAL)
            text_area.insert(tk.END, message + '\n')
            text_area.config(state=tk.DISABLED)
        except:
            print("Error receiving message.")
            client_socket.close()
            break

# Function to send messages to the server
def send_message(client_socket, message_entry):
    message = message_entry.get()
    if message:
        client_socket.send(message.encode())
        message_entry.delete(0, tk.END)

# GUI Setup function
def setup_gui(client_socket):
    # Create the root window
    root = tk.Tk()
    root.title("Client Chat")

    # Text area for displaying chat messages
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
    text_area.pack(padx=10, pady=10)

    # Text entry for typing messages
    message_entry = tk.Entry(root, width=50)
    message_entry.pack(padx=10, pady=10)

    # Button to send message
    send_button = tk.Button(root, text="Send", command=lambda: send_message(client_socket, message_entry))
    send_button.pack(pady=5)

    # Binding Enter key to send message
    message_entry.bind("<Return>", lambda event: send_message(client_socket, message_entry))

    # Thread for receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket, text_area))
    receive_thread.daemon = True
    receive_thread.start()

    # Start the Tkinter main loop
    root.mainloop()

# Main function to start the client
def main():
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server (localhost in this case)
        client_socket.connect(('127.0.0.1', 9999))

        # Call the GUI setup function
        setup_gui(client_socket)

    except Exception as e:
        messagebox.showerror("Connection Error", f"Unable to connect to server: {e}")

if __name__ == "__main__":
    main()
