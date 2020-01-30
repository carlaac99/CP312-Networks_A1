# Import socket module
from socket import * 
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
boardWidth = int(sys.argv[2])   # Width of board
boardHeight = int(sys.argv[3])  # Height of board
print("board width: ", boardWidth)
print("board height: ", boardHeight)
colour_string=""
board = []

for i in range(4, 8):
    colour_var = sys.argv[i].upper()
    colour_string += colour_string + " " + colour_var
    
print(colour_string)
    
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
        
       
        
        x = int(sent[1])
        y = int(sent[2])
        width = int(sent[3])
        height = int(sent[4])
        
        colour = sent[5]
        
        
        note= Note(x, y,width, height, colour,new_message,0)

        result = 'POST'
        
        if ((x+ width) <= boardWidth) and ((y + height) <= boardHeight):
            
            if (colour_string.__contains__(colour)):
                result = 'POST'
                Board.append(note)
            else:
                result = "Choose colour that is available for note"
        else:
            print(x+y)
            result = x+y
        
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
