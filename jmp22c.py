# Name: Justin Meman
# Due Date: 3/29/2021

from socket import *
import time

serverName = '127.0.0.1'
clientSocket = socket(AF_INET, SOCK_DGRAM)

heartbeatCount = 0
secEnd = 5

while True:
    message = str(heartbeatCount)
    print("Heartbeat pulse %d" % (heartbeatCount))
    clientSocket.sendto(message.encode(), (serverName, 45678))
    heartbeatCount += 1
    time.sleep(secEnd)