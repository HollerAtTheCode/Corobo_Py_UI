import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.178.48', 5001))
s.send(bytes("A1","utf-8"))
s.close()