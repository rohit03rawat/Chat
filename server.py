import tkinter as tk
import socket
import threading

class ChatServerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Server")
        
        self.text_area = tk.Text(root)
        self.text_area.pack(expand=True, fill='both')
        
        self.start_button = tk.Button(root, text="Start Server", command=self.start_server)
        self.start_button.pack()
        
        self.server_thread = None
        self.server_socket = None

    def start_server(self):
        if not self.server_thread:
            self.server_thread = threading.Thread(target=self.run_server)
            self.server_thread.start()

    def run_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', 9999))
        self.server_socket.listen(5)
        self.text_area.insert(tk.END, "Server started and listening on port 9999\n")
        
        while True:
            client_socket, addr = self.server_socket.accept()
            self.text_area.insert(tk.END, f"Connection from {addr}\n")
            while True:
                try:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    self.text_area.insert(tk.END, f"Received: {data.decode()}\n")
                    client_socket.send(data)
                except:
                    break
            client_socket.close()
            self.text_area.insert(tk.END, "Client disconnected\n")

root = tk.Tk()
app = ChatServerGUI(root)
root.mainloop()

