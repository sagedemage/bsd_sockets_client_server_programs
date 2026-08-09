# Async echo server program
import socket
import asyncio

HOST = ""
PORT = 8080

async def main():
    # Socket Address Families:
    # 1. AF_INET: IPv4 Address
    # 2. AF_INET6: IPv6 Address
    # 3. AF_UNIX: Socket bound to a special file on a filesystem. It is similar to a loopback device.
    # It does not have to pass through the TCP/IP network stack.

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        sock.setblocking(False)
        print("Server listening on 127.0.0.1:8080")

        loop = asyncio.get_running_loop()
        while True:
            conn, addr = await loop.sock_accept(sock)
            with conn:
                c_addr = addr[0]
                c_port = addr[1]
                print("Connected by", f"{c_addr}:{c_port}")

                while True:
                    data = await loop.sock_recv(conn, 1024)
                    if data == b'':
                        # Client disconnected. Closing the connection.
                        # You should close the conenction to prevent
                        # the "Address already in" use error
                        break
                    else:
                        await loop.sock_sendall(conn, data)
                        print(data)
                        print("")

if __name__ == "__main__":
    asyncio.run(main())