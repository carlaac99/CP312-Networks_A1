'''
Created on Jan. 28, 2020

@author: nicolelaslavic
'''
# Imports socket module
from socket import * 
import sys # In order to terminate the program

boardWidth = int(sys.argv[2])   # Width of board
boardHeight = int(sys.argv[3])  # Height of board
print("board width: ", boardWidth)
print("board height: ", boardHeight)
colour_string = []
Board = []

#change to while loop
for i in range(4, 8):
    colour_var = sys.argv[i].upper()
    colour_string.append(colour_var)
print(colour_string)

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(10)

print ('The server is ready to receive')

# Server should be up and running and listening to the incoming connections

class Note(object):
    message= ""
    colour = ""
    x = 0
    y =0
    height=0
    width=0
    pins = 0

    # The class "constructor" - It's actually an initializer 
    def __init__(self, x, y, width,height,colour,message, pins):
        self.message = message
        self.colour = colour
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.pins = pins
    def __str__(self):
        return "%s" % (self.message)

while True:
    #print('The server is ready to receive')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(2048).decode()

    sent=sentence.split()

    request= sent[0].upper()
    
    if request=='PIN':
        
        result = 'PIN'
    
        #do something
    elif request=='GET':
        all_on_board = ""
        for i in Board:
            all_on_board = all_on_board + Board[i]
         
        if all_on_board != "":
            result = all_on_board
        else:
            result = "board is empty"
        
            #do something
    elif request == 'UNPIN':
        print("UNPIN")
        result = "UNPIN"
            #do something
    
    elif request =='POST':
        cb =' '
        new_message= cb.join(sent[6:])
        x = int(sent[1])
        y = int(sent[2])
        width = int(sent[3])
        height = int(sent[4])
        colour = sent[5].upper()
        note= Note(x, y,width, height, colour,new_message, 0)
        sent = ""

        incolour=False

        if ((x+ width) <= boardWidth) and ((y + height) <= boardHeight):
            for i in colour_string:
                
                if (i==colour):
                    incolour=True
            
            if(incolour==True):
                Board.append(note)
                result= str(new_message)
            else:
                result="it could not be appended"  
        else:
            print(x+y)
            result = x+y

    elif request == 'CLEAR':
        result = "CLEAR"
    
    elif request=='CONNECT':
        
        result = "connecting"
            #do something
    elif request=='DISCONNECT':
        
        result = "disconnecting"
        serverSocket.close()
        connectionSocket.close()
        sys.exit()#Terminate the program after sending the corresponding data
            #do something
    else:
        result="nothing"
    
      
        #capitalizedSentence = sentence.upper()
  
        
        
    connectionSocket.send(result.encode())
    
    
        
