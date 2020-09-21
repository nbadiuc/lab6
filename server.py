import socket
import sys
import os

server_address = ('', 9324) 
server = socket.socket(socket.AF_INET)
server.bind(server_address)
server.listen(10)

while (True):
    sc, client_address = server.accept()
    filename = sc.recv(1024).decode("utf-8")
    
    ls = os.listdir('.')
    if filename in ls:
        for i in range(len(filename)):
            if filename[i] == ".":
                break
        name = filename[:i]
        extension = filename[i+1:]
        copy_num = 1
        while (filename in ls):
            filename = name + "_copy" + str(copy_num) + "." + extension
            copy_num += 1
    
    f = open(filename,'wb')
    l = sc.recv(1024) 
    while (l):
        f.write(l)
        l = sc.recv(1024)

    f.close()
    sc.close()

server.close()
