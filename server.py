# Echo Server Program
import socket

HOST = ""
PORT = 8080

def main():
    # Socket Address Families:
    # 1. AF_INET: IPv4 Address
    # 2. AF_INET6: IPv6 Address
    # 3. AF_UNIX: Socket bound to a special file on a filesystem. It is similar to a loopback device.
    # It does not have to pass through the TCP/IP network stack.

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        print("Server listening on 127.0.0.1:8080")

        while True:
            conn, addr = sock.accept()
            with conn:
                c_addr = addr[0]
                c_port = addr[1]
                print("Connected by", f"{c_addr}:{c_port}")

                while True:
                    data = conn.recv(1024)
                    if data == b'':
                        # Client disconnected. Closing the connection.
                        # You should close the conenction to prevent
                        # the "Address already in use" error
                        break
                    else:
                        conn.sendall(data)
                        print(data)
                        print("")

if __name__ == "__main__":
    main()