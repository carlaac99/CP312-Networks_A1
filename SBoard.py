# Import socket module
from socket import * 
import sys # In order to terminate the program


boardWidth = sys.argv[2]    # Width of board
boardHeight = sys.argv[3]  # Height of board
print("board width: ", boardWidth)
print("board height: ", boardHeight)
colour_list = []
board = []

for i in range(4, 8):
    print("colour: ", sys.argv[i])
    colour_var = sys.argv[i].upper()
    colour_list.append(colour_var)
  

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


class note(object):
    message= ""
    colour = ""
    x = 0
    y=0
    height=0
    width=0

    # The class "constructor" - It's actually an initializer 
    def init(self, x, y, width,height,colour,message):
        self.message = message
        self.colour = colour
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        
    
        result = "GET"
            #do something
    elif request == 'UNPIN':
        print("UNPIN")
        result = "UNPIN"
            #do something
    
    elif request =='POST':
        note.x = sent[1]
        note.y = sent[2]
        note.width = sent[3]
        note.height = sent[4]
        note.colour = sent[5].upper()
        note.message = sent[6].upper()
        result = "note.x"
#         if ((note.x + note.width) <= boardWidth) and ((note.y + note.height) <= boardHeight):
#             if (colour_list.contains(note.colour)):
#                 result = 'POST'
#                 board.append(note.message)

#             else:
#                 result = "Choose colour that is available for note"
#         else:
#             result = 'note not within the board parameters'
    elif request == 'CLEAR':
        result = "CLEAR"
    
    elif request=='CONNECT':
    
        
        result = "connecting"
            #do something
    elif request=='DISCONNECT':
        
        result = "disconnecting"
        serverSocket.close()
            #do something
    else:
        result="nothing"
    
      
        #capitalizedSentence = sentence.upper()
  
        
        
    connectionSocket.send(result.encode())
    connectionSocket.close()
    
        
sys.exit()#Terminate the program after sending the corresponding data
