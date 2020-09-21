import socket
import sys
from pathlib import Path

filename = sys.argv[1]
server_address = (sys.argv[2], int(sys.argv[3]))

s = socket.socket(socket.AF_INET)
s.connect(server_address)
s.send(bytes(filename, 'utf-8'))
file = open (filename, "rb")

filesize = Path(filename).stat().st_size
currentfilesize = 0
    
for i in range((filesize + 1023) // 1024):
    l = file.read(1024)
    currentfilesize += 1024
    s.send(l)
    if (i % 100 == 0):
        print(str(currentfilesize / filesize * 100) + "%") # our progress bar
        
s.close()
