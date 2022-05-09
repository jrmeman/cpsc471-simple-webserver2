# Name: Justin Meman
# Due Date: 3/29/2021

from socket import *
import sys
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 45678))
serverSocket.settimeout(10)

while True:
    start = time.time()

    try:
        message, address = serverSocket.recvfrom(1024)
        end = time.time()
        elapsed = round((end - start), 5)
        print(f"Server received heartbeat pulse {message.decode()}. Pulse interval was {elapsed} seconds.")
        start = time.time()
    except timeout:
        print("No pulse after 10 seconds. Server quits")
        print("Server stops.")
        serverSocket.close()
        sys.exit()

    serverSocket.sendto(message, address)
