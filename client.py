import socket
import sys

REMOTE_HOST = "192.168.182.129"
LOCAL_HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    try:
        sock.connect(((REMOTE_HOST, PORT)))
    except ConnectionRefusedError:
        sys.exit("Error: Server is not open!")
    
    sock.sendall(b'Hello, world')
    data = sock.recv(1024)

print('Received', repr(data))