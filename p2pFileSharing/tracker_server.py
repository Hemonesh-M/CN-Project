import socket
import threading

peers = {}  # filename -> list of (ip, port)

def handle_client(conn, addr):
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break

            cmd = data.split()
            if cmd[0] == "REGISTER":
                filename = cmd[1]
                port = int(cmd[2])
                if filename not in peers:
                    peers[filename] = []
                peers[filename].append((addr[0], port))
                conn.send(b"REGISTERED")
            elif cmd[0] == "GET":
                filename = cmd[1]
                peer_list = peers.get(filename, [])
                response = "\n".join([f"{ip} {port}" for ip, port in peer_list])
                conn.send(response.encode() if response else b"NONE")
        except:
            break
    conn.close()

s = socket.socket()
s.bind(("0.0.0.0", 8000))
s.listen(5)
print("Tracker running on port 8000...")

while True:
    conn, addr = s.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
