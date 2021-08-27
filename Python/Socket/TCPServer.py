import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
        c, addr = s.accept()
        print('ip: ', addr)
        print(c.recv(1024).decode())
        #c.send('good condition'.encode())
        c.close()