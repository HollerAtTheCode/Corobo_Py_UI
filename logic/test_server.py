from socket import socket, gethostbyname, AF_INET, SOCK_STREAM,SO_REUSEADDR,SOL_SOCKET
import os
SERVER_IP = '192.168.178.23'
PORT = 5001
s = socket(AF_INET, SOCK_STREAM)


hostName = gethostbyname('0.0.0.0')
print(hostName)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((hostName, PORT))
s.listen(5)
print("Test server listening on port {0}\n".format(PORT))
while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print('Server Ready')
    info = clientsocket.recv(1024)
    msg = "python try.py " + info.decode("utf-8")
    print(msg)
    os.system(msg)
