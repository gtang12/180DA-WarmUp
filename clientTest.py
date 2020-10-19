import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.116', 8081)) # replaced 0.0.0.0 with server IP
client.send("I am CLIENT\n".encode())
from_server = client.recv(4096).decode('utf-8')
client.close()
print(from_server)
