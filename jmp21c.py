# Name: Justin Meman
# Due Date: 3/29/2021

import socket
from socket import AF_INET, SOCK_DGRAM
import time
import datetime

packetLoss = 0
MaxRTT = 0
MinRTT = 1000
Sum = 0

serverName = '127.0.0.1'
clientSocket = socket.socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
sequence_number = 1

while sequence_number <= 15:
    message = 'Ping'
    start = time.time()
    clientSocket.sendto(message.encode(), (serverName, 45678))

    try:
        message, address = clientSocket.recvfrom(1024)
        receivedTime = time.time() - start
        elapsed = (time.time() - start)
        RTT = (time.time() - start) * 1000
        Sum = Sum + RTT
        if RTT > MaxRTT:
            MaxRTT = RTT
        if RTT < MinRTT:
            MinRTT = RTT
        now = datetime.datetime.now()
        print("Ping %s: host %s replied: " % (sequence_number, serverName) + now.strftime("%m-%d-%Y %H:%M:%S") + " RTT=%f ms" % (RTT))

    except socket.timeout:
        print("Ping %s: timed out, message was lost" % sequence_number)
        packetLoss = packetLoss + 1
    
    sequence_number += 1
    if sequence_number > 15:
        clientSocket.close()

if __name__ == '__main__':
    Lost = packetLoss / 10
    AverageRTT = Sum / (10 - packetLoss)
    print('Min RTT = %f ms' % MinRTT)
    print('Max RTT = %f ms' % MaxRTT)
    print('Average RTT = %f ms' % AverageRTT)
    print(f'Packet loss = {Lost * 100} %')