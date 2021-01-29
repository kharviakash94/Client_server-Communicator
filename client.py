import socket
import time


def myfunction():

    c = socket.socket()
    c.connect(("localhost", 5555))
    print(c.recv(1024).decode())


while True:
    try:
        myfunction()
        time.sleep(5.0)

    except ConnectionRefusedError:
        print("Bye Connection Over")
        break















