import socket
import sys
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket created")
except:
    print("failed to create socket")
    sys.exit()
print("connecting")
full_msg = ''
host_IP = input("Enter Host IP")
s.connect((host_IP, 8008))
# s.send(bytes("connected","utf-8"))
# print(s.recv(1024).decode())
while 1:
    txt = input("CMD: ")
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_IP, 8008))
    s.sendall(bytes(txt,"utf-8"))
    while 1:
        msg = s.recv(1024).decode()
        full_msg = full_msg+msg
        if  len(msg) <=0:
            break
    print(full_msg)
    full_msg=''
