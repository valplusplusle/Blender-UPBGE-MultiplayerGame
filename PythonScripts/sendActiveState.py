import bge
import socket
import time

controller = bge.logic.getCurrentController()
obj = controller.owner
scene = bge.logic.getCurrentScene()

playerID = str(obj['ID'])
myTime = time.time()

msgFromClient       = "activeTime,"+str(playerID)+","+str(myTime)
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)