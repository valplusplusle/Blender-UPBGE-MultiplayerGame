import bge
import socket
import time

controller = bge.logic.getCurrentController()
obj = controller.owner
scene = bge.logic.getCurrentScene()


playerID = str(obj['ID'])

myPosX = str(scene.objects["Cube.001"].localPosition.x)
myPosY = str(scene.objects["Cube.001"].localPosition.y)
myPosZ = str(scene.objects["Cube.001"].localPosition.z)
#print (myPosX, myPosY, myPosZ)

msgFromClient       = playerID+","+myPosX+","+myPosY+","+ myPosZ
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)