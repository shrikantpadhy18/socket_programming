import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client_socket.settimeout(1.0)
addr = ("127.0.0.1", 3000)
client_socket.connect(addr)
while True:
    data, server = client_socket.recv(4096)    
    print(data)
