# Import socket module
import threading
from socket import * 
import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
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
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time


print ('The server is ready to receive')

class ClientThread(threading.Thread):
    
    def __init__(self,addr,clientsocket):
        
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", addr)
    def run(self):
        print ("Connection from : ", addr)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
 
        while True:
            sentence= self.csocket.recv(2048).decode()
            
            print ("from client", sentence)
            #self.csocket.send(bytes(sentence,'UTF-8'))
            print ("Client at ", addr , " disconnected...")
        
            sent=sentence.split()
            
            request= sent[0]
            
            if request=='PIN':
                x= int(sent[1])
                y=int(sent[2])
                
                for i in Board:
                    if i.x==x and i.y==y:
                        i.pins+=1
                
                print("PIN")
                result = 'PIN'
                
                
                #do something
            elif request=='GET': #change so user could request all at once
                             
                all_on_board = ""
                results_array = []
                
                if(len(sent) == 2):
                    for f in Board:
                        all_on_board = all_on_board + str(f) + ", "
                else:
                    for p in Board:
                        results_array.append(p)
                
                    for i in range (0,len(sent)):
                    
                        user_get =sent[i].upper()
                    
                        print("\nuser_get",user_get)
                    
                        if (user_get == 'COLOUR='):
                            
                            colour_choice = sent[i+1].upper()
                            for c in results_array:
                                colourr = str(c.colour)
                                if(colourr != colour_choice):
                                    results_array.remove(c)
                                    
                        #fix
                        elif(user_get == 'CONTAINS='):
                            x = sent[i+1]
                            y = sent[i+2]
                            
                            for k in results_array:
                                results_array.append(k.x)
                                results_array.append(k.y)
                                results_array.append(x)
                                results_array.append(y)
#                                 if(k.x != x_cord or y_cord != k.y):
#                                     results_array.remove(k)
        
                                    
                        elif (user_get == 'REFERSTO='):
                            keyword = sent[i+1]
                            for j in results_array:
                                if keyword not in j.message: 
                                    results_array.remove(j)
                            
                        #fix
                        elif(user_get == 'PINS='):
                            for a in results_array:
                                if(int(a.pins) < 1):
                                    results_array.remove(a)
                
                for n in results_array:
                    all_on_board = all_on_board + str(n) + ", "
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
                
                colour = sent[5].upper()
                
                incolour=False
                
                note= Note(x, y, width, height, colour, new_message, 0)
        
                #result = 'POST'
                
                if ((x+ width) <= boardWidth) and ((y + height) <= boardHeight):
                    
                    for i in colour_string:
                        
                        if (i==colour):
                            incolour=True
                    
                    if(incolour==True):
                        Board.append(note)
                        result="it has been appended" 
                    else:
                        result="it could not be appended"  
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
            
                connectionSocket.close()
                serverSocket.close()  
                sys.exit()
                #do something
            elif request== 'CLEAR':
                
                for i in Board:
                    Board.pop(i)
                    
                result='Board now clear'
                
            else:
                result="nothing"
                
            connectionSocket.sendall(result.encode())

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
        
   def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.x, self.y, self.width, self.height, self.colour, self.message, self.pins)
    
        
Board=[]
while True:
    #print('The server is ready to receive')
    serverSocket.listen(1)
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    
    #sentence = connectionSocket.recv(1024).decode()
    
    newthread = ClientThread(addr, connectionSocket)
    newthread.start()
    
    
        
