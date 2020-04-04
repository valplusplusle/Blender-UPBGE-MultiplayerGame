import socket
import time

w, h = 4, 4;
Matrix = [[0 for x in range(w)] for y in range(h)]
Active = [[0 for x in range(w-2)] for y in range(h)]

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
# Listen for incoming datagrams

while(True):
    print (Matrix)
    print (Active)
    msgFromServer       = "Online"
    bytesToSend         = str.encode(msgFromServer)

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = format(message)
    splittedMsg = clientMsg.split(',')

    if clientMsg == "getPositions":
        #Send all Pos data from all players as anwser
        positionPlayer       = str(Matrix)
        bytespositionPlayer  = str.encode(positionPlayer)
        UDPServerSocket.sendto(bytespositionPlayer, address)

    elif splittedMsg[0] == "activeTime":
        clientAlreadyActive = False
        for i in range(len(Active)):
            if Active[i][0] == splittedMsg[1]:
                Active[i][1]= splittedMsg[2]
                clientAlreadyActive = True
        if clientAlreadyActive == False:
            for i in range(len(Active)):
                if Active[i][0] == 0 and clientAlreadyActive == False:
                    Active[i][0]= splittedMsg[1]
                    Active[i][1]= splittedMsg[2]
                    clientAlreadyActive = True
    else:
        #Get pos data from the player and save it to the player list
        positionData = clientMsg.split(',')
        playerId = positionData[0]
        posX = positionData[1]
        posY = positionData[2]
        posZ = positionData[3]
        clientAlreadyAvailable = False

        for i in range(len(Matrix)):
            if Matrix[i][0] == playerId:
                Matrix[i][1]= posX
                Matrix[i][2]= posY
                Matrix[i][3]= posZ
                clientAlreadyAvailable = True

        if clientAlreadyAvailable == False:
            addNewClientStatus = False
            for i in range(len(Matrix)):
                if Matrix[i][0] == 0:
                    Matrix[i][0]= playerId
                    Matrix[i][1]= posX
                    Matrix[i][2]= posY
                    Matrix[i][3]= posZ
                    print("add new client")
                    addNewClientStatus = True
                    break
            if addNewClientStatus == False:
                serverInfo       = "Server Full"
                bytesToSend      = str.encode(serverInfo)
                print("server full")
        UDPServerSocket.sendto(bytesToSend, address)

    timeNow = float(time.time())
    for i in range(len(Active)):
        if Active[i][1] != 0:
            timeSend = float(Active[i][1])
            if timeSend < (timeNow-10):
                idToDelete = Active[i][0]
                for j in range(len(Matrix)):
                    if Matrix[j][0] == idToDelete:
                        Matrix[j][0] = 0
                        Matrix[j][1] = 0
                        Matrix[j][2] = 0
                        Matrix[j][3] = 0
                Active[i][0] = 0
                Active[i][1] = 0
                
