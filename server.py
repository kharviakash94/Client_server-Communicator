import socket
from datetime import datetime

s = socket.socket()
print("socket created")
s.bind(("localhost", 5555))
s.listen(3)
print("waiting for connections")

while True:
    c, addr = s.accept()
    p = datetime.now().isoformat()
    print("connected with", addr)
    c.send(bytes(p, 'utf-8'))
    c.close()

