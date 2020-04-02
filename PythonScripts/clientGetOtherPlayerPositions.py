import bge
import socket

msgFromClient       = "getPositions"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = format(msgFromServer[0])

msglist = msg.replace("'", "")
msglist = msglist.replace("b", "")
msglist = msglist.replace("[", "")
msglist = msglist.replace("]", "")
msglist = msglist.replace('"', "")
msglist = msglist.split(", ")

w, h = 4, 2;
Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[0][0] = msglist[0]
Matrix[0][1] = msglist[1]
Matrix[0][2] = msglist[2]
Matrix[0][3] = msglist[3]

Matrix[1][0] = msglist[4]
Matrix[1][1] = msglist[5]
Matrix[1][2] = msglist[6]
Matrix[1][3] = msglist[7]

controller = bge.logic.getCurrentController()
obj = controller.owner
scene = bge.logic.getCurrentScene()
playerID = str(obj['ID'])

for i in range(len(Matrix)):
    if Matrix[i][0] != playerID:
        test = 2
        controller = bge.logic.getCurrentController()
        obj = controller.owner
        scene = bge.logic.getCurrentScene()
        scene.objects["Cube.00"+str(test)].localPosition = [float(Matrix[i][1]), float(Matrix[i][2]), float(Matrix[i][3])]