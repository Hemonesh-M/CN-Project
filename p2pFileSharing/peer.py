import socket
import os
import threading

TRACKER_IP = '127.0.0.1'
TRACKER_PORT = 8000

# Ask user for peer port and folder
peer_port = int(input("Enter your peer port (e.g., 9001): "))
SHARE_FOLDER = input("Enter your shared folder path (e.g., ./filesA): ").strip()
os.makedirs(SHARE_FOLDER, exist_ok=True)

def serve_files():
    s = socket.socket()
    s.bind(('', peer_port))
    s.listen(5)
    while True:
        conn, addr = s.accept()
        filename = conn.recv(1024).decode()
        filepath = os.path.join(SHARE_FOLDER, filename)
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                data = f.read()
                conn.sendall(data)
        conn.close()

def register_file(filename):
    s = socket.socket()
    s.connect((TRACKER_IP, TRACKER_PORT))
    msg = f"REGISTER {filename} {peer_port}"
    s.send(msg.encode())
    response = s.recv(1024).decode()
    print(response)
    s.close()

def download_file(filename):
    s = socket.socket()
    s.connect((TRACKER_IP, TRACKER_PORT))
    msg = f"GET {filename}"
    s.send(msg.encode())
    response = s.recv(1024).decode()
    s.close()

    if response == "NOT FOUND":
        print("File not found on tracker.")
        return

    peer_ip, peer_port_str = response.split()
    peer_port = int(peer_port_str)

    peer_sock = socket.socket()
    peer_sock.connect((peer_ip, peer_port))
    peer_sock.send(filename.encode())
    data = b""
    while True:
        chunk = peer_sock.recv(4096)
        if not chunk:
            break
        data += chunk
    peer_sock.close()

    filepath = os.path.join(SHARE_FOLDER, filename)
    with open(filepath, 'wb') as f:
        f.write(data)
    print(f"Downloaded {filename} from {peer_ip}:{peer_port}")

# Start file server thread
threading.Thread(target=serve_files, daemon=True).start()

# Menu
while True:
    print("\n1. Register File\n2. Download File\n3. Exit")
    choice = input("Choice: ")
    if choice == '1':
        filename = input("Filename (in your folder): ")
        if os.path.exists(os.path.join(SHARE_FOLDER, filename)):
            register_file(filename)
        else:
            print("❌ File not found in your folder!")
    elif choice == '2':
        filename = input("Filename to download (eg. cat.jpg): ")
        download_file(filename)
    elif choice == '3':
        break
    else:
        print("Invalid choice.")
