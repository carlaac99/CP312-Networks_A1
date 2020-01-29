# Import socket module
from socket import * 
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

print ('The server is ready to receive')

# Server should be up and running and listening to the incoming connections
class Note(object):
    message= ""
    colour = ""
    x = 0
    y=0
    height=0
    pins=0
    width=0

    # The class "constructor" - It's actually an initializer ,pin
    def __init__(self, x, y, width,height, colour,message,pins):
        self.message = message
        self.colour = colour
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.pins=pins
        
Board=[]
while True:
    #print('The server is ready to receive')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    
    sentence = connectionSocket.recv(1024).decode()
    
    sent=sentence.split()
    
    request= sent[0].upper()
    
    if request=='PIN':
        print("PIN")
        result = 'PIN'
        
        #do something
    elif request=='GET':
        print("GET")
        
        result = "GET"
        #do something
    elif request == 'UNPIN':
        print("UNPIN")
        result = "UNPIN"
        #do something
        
    elif request =='POST':
        print("POST")
        cb =' '
        new_message= cb.join(sent[6:])
        
        note= Note(sent[1], sent[2],sent[3], sent[4], sent[5],new_message,0)
        Board.append(note)

        result = 'POST'
        
    elif request=='CONNECT':
        
        print("connecting")
        result = "connecting"
        #do something
    elif request=='DISCONNECT':
        
        print("DISCONNECT")
        result = "disconnecting"
        #do something
    elif request== 'CLEAR':
        
        for i in Board:
            Board.pop(i)
            
        result='Board now clear'
        
    else:
        result="nothing"
        
    connectionSocket.sendall(result.encode())

    
    connectionSocket.close()



serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
