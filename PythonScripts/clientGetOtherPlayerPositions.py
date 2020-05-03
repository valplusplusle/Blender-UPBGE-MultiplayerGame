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
print(msglist)
w, h = 4, 4;
Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[0][0] = msglist[0]
Matrix[0][1] = msglist[1]
Matrix[0][2] = msglist[2]
Matrix[0][3] = msglist[3]

Matrix[1][0] = msglist[4]
Matrix[1][1] = msglist[5]
Matrix[1][2] = msglist[6]
Matrix[1][3] = msglist[7]

Matrix[2][0] = msglist[8]
Matrix[2][1] = msglist[9]
Matrix[2][2] = msglist[10]
Matrix[2][3] = msglist[11]

Matrix[3][0] = msglist[12]
Matrix[3][1] = msglist[13]
Matrix[3][2] = msglist[14]
Matrix[3][3] = msglist[15]

controller = bge.logic.getCurrentController()
obj = controller.owner
scene = bge.logic.getCurrentScene()
playerID = str(obj['ID'])

if Matrix[0][0] != playerID:
    controller = bge.logic.getCurrentController()
    obj = controller.owner
    scene = bge.logic.getCurrentScene()
    scene.objects["Cube.000"].localPosition = [float(Matrix[0][1]), float(Matrix[0][2]), float(Matrix[0][3])]

if Matrix[1][0] != playerID:
    controller = bge.logic.getCurrentController()
    obj = controller.owner
    scene = bge.logic.getCurrentScene()
    scene.objects["Cube.001"].localPosition = [float(Matrix[1][1]), float(Matrix[1][2]), float(Matrix[1][3])]

if Matrix[2][0] != playerID:
    controller = bge.logic.getCurrentController()
    obj = controller.owner
    scene = bge.logic.getCurrentScene()
    scene.objects["Cube.002"].localPosition = [float(Matrix[2][1]), float(Matrix[2][2]), float(Matrix[2][3])]

if Matrix[3][0] != playerID:
    controller = bge.logic.getCurrentController()
    obj = controller.owner
    scene = bge.logic.getCurrentScene()
    scene.objects["Cube.003"].localPosition = [float(Matrix[3][1]), float(Matrix[3][2]), float(Matrix[3][3])]
