import socket

s = socket.socket()
host = '10.59.173.219'
port = 12345

s.connect((host, port))
message = raw_input()
s.send(message.encode())
s.close()