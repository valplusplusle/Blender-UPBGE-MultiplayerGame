import socket

w, h = 4, 4;
Matrix = [[0 for x in range(w)] for y in range(h)]

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Online"
bytesToSend         = str.encode(msgFromServer)

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")
# Listen for incoming datagrams

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = format(message)
    if(clientMsg == "getPositions"):
        #Send all Pos data from all players as anwser
        positionPlayer       = str(Matrix)
        bytespositionPlayer  = str.encode(positionPlayer)
        print (positionPlayer)
        print (bytespositionPlayer)
        UDPServerSocket.sendto(bytespositionPlayer, address)
    else:
        #Get pos data from the player and save it to the player list
        positionData = clientMsg.split(',')
        playerId = positionData[0]
        posX = positionData[1]
        posY = positionData[2]
        posZ = positionData[3]
        for i in range(len(Matrix)):
            if Matrix[i][0] == playerId:
                Matrix[i][1]= posX
                Matrix[i][2]= posY
                Matrix[i][3]= posZ
                break
            if Matrix[i][0] == 0:
                Matrix[i][0]= playerId
                Matrix[i][1]= posX
                Matrix[i][2]= posY
                Matrix[i][3]= posZ                
                break
        UDPServerSocket.sendto(bytesToSend, address)