# ConvoSpace – Local Network Chat Application 💬

A lightweight terminal-based chat application using Python's socket programming.  
Supports both localhost and LAN-based chat over a shared Wi-Fi network.

## 🔧 Features

- Client-server architecture using Python sockets  
- Real-time messaging between users  
- Supports both localhost and LAN (Wi-Fi) communication  
- Multithreaded server handles multiple clients  
- Command-line interface for ease of use

## 🗂️ Project Structure

Chat/  
├── localhost/         # Basic version for single client communication  
│   ├── server.py  
│   ├── client.py  
│   └── index.html     # Optional browser test page  
│  
├── network/           # LAN version supporting multiple clients  
│   ├── server.py  
│   └── client.py  

## ▶️ How to Run (LAN Version)

1. Run the server:  
   python network/server.py

2. On another terminal or device connected to the same Wi-Fi:  
   python network/client.py

⚠️ Make sure to update the IP address in the `client.py` file to match the server’s IP.

## 📚 Requirements

- Python 3.x  
- No external libraries required (only `socket` and `threading` from the standard library)

## 👨‍💻 Author

**Rohit Rawat** – Backend & Network Enthusiast  
LinkedIn: https://linkedin.com/in/your-profile-link

## 📌 Notes

This project was part of my personal learning journey to explore backend communication and socket-level networking in Python.  
Still evolving and open to further improvements!
