# Import socket module
import threading
from socket import * 

import sys # In order to terminate the program

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
print_lock = threading.Lock() 
boardWidth = int(sys.argv[2])   # Width of board
boardHeight = int(sys.argv[3])  # Height of board
print("board width: ", boardWidth)
print("board height: ", boardHeight)

colour_string = []
Board = []
Pins = []

#change to while loop
for i in range(4,len(sys.argv)):
    colour_var = sys.argv[i].upper()
    colour_string.append(colour_var)
print(colour_string)


serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

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
        print ("\nNew connection added: ", addr)
        
    def run(self):
        print ("\nConnection from : ", addr)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))

        while True:


            sentence= self.csocket.recv(2048).decode()

            
            print ("from client: ", sentence)
            #self.csocket.send(bytes(sentence,'UTF-8'))

            sent=sentence.split()
            
            try:
                request= sent[0]
            except IndexError as e:
                result=e

            if request=='PIN':
                try:
                    x= int(sent[1])
                    y=int(sent[2])
                                   
                    for i in Board:
                        if i.x==x and i.y==y:
                            i.pins+=1

                    result = 'PIN'
                
                except(IndexError,ValueError) as e:
                    result= "an error occurred"
 
                
                #do something
            elif request=='GET':
                try:
                    all_on_board = ""
                    results_array = []
                    
                    if(len(sent) == 2 and sent[1].upper() != 'PINS'):
                        if(sent[1].upper() == "COLOUR=" or sent[1].upper() == "CONTAINS=" or sent[1].upper() == "REFERSTO="):
                            if(len(Board) == 0):
                                results_array = ["Board is empty"]
                            else:
                                for f in Board:
                                    all_on_board = all_on_board + str(f) + ", "
                        else:
                            results_array = ["Please choose an appropriate option"]
                    else:
                        results_array = Board.copy()
                        for i in range (0,len(sent)):
                        
                            user_get =sent[i].upper()
                        
                            print("\nuser_get",user_get)
                        
                            if (user_get == 'COLOUR='):
                                
                                colour_choice = sent[i+1].upper()
                                index = 0
                                while(index < len(results_array)):
                                    colourr = str(results_array[index].colour)
                                    if(colourr != colour_choice):
                                        results_array.pop(index)
                                        index = index -1
                                    index = index + 1
                
                                 
                            elif(user_get == 'CONTAINS='):
                                x = int(sent[i+1])
                                y = int(sent[i+2])
                                index = 0
                                
                                while (index < len(results_array)):
                                    if(results_array[index].x != x and y!= results_array[index].y):
                                        results_array.pop(index)
                                        index = index - 1
                                    index = index + 1
            
                            elif (user_get == 'REFERSTO='):
                                keyword = sent[i+1]
                                index = 0
                                while (index < len(results_array)):
                                    if keyword not in results_array[index].message: 
                                        results_array.pop(index)
                                        index = index -1
                                    index=index+1
                                
                            elif(user_get == 'PINS'):
                                if len(Pins) == 0:
                                    results_array = ["None"]
                                else:
                                    index = 0
                                    while(index < len(results_array)):
                                        if(results_array[index].pins < 1):
                                            results_array.pop(index)
                                            index = index - 1
                                        index = index + 1
                                    
                    
                    for n in results_array:
                        all_on_board = all_on_board + str(n) + ", "
                        
                    result = all_on_board
                         
                except (IndexError,ValueError):
                    result= "an error occured"
                             

                    
            elif request == 'UNPIN':
                
                try:
                              
                    x = int(sent[1])
                    y = int(sent[2])
                    for i in Board:
                        if i.x==x and i.y==y and i.pins>0:
                            i.pins-=1
      
                    result = "UNPIN"
                    
                except (IndexError,ValueError):
                    result="An ERROR has occured: please enter integer values"

            elif request =='POST':


                cb =' '

                try:
                    x = int(sent[1])
                    y = int(sent[2])
                    width = int(sent[3])
                    height = int(sent[4])
                    new_message= cb.join(sent[6:])
                                    
                    colour = sent[5].upper()

                    

                    incolour=False
                    
                    note= Note(x, y, width, height, colour, new_message, 0)
            
                    #result = 'POST'
                    
                    if ((x+ width) <= boardWidth) and ((y + height) <= boardHeight and (x+width) >= 0 and (y+height) >= 0 and x>0 and y>0):
                        
                        for i in colour_string:
                            
                            if (i==colour):
                                incolour=True
                        
                        if(incolour==True):
                            Board.append(note)
                            result="it has been appended" 
                        else:
                            result="it could not be appended"  
                    else:
                        result = "coordinates not on board, not appended"
                        

                    
                except (IndexError,ValueError):
                    result="an error has occured please try again"
                
            elif request=='CONNECT':
                
      
                result="\nnote colours: "
                for i in colour_string:
                    result=result+i+" "
                result+="\nBoard width: "+ str(boardWidth) +" Board Height: " + str(boardHeight)

            elif request=='DISCONNECT':
                
                print("DISCONNECT")
                result = "disconnecting"
            
                connectionSocket.close()
                break
                #do something
            elif request== 'CLEAR':

                i=0
                if(len(Board) != 0):
                    while(i< len(Board)):
                        if Board[i].pins==0:
                            Board.pop(i)
                            i=i-1
                        i=i+1
                        
                    result="Board now clear"
                    
                else:
                    result="Board is empty cannot clear."
            
            self.csocket.sendall(result.encode())



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
        return "x-cord: %s y-cord: %s width: %s height: %s colour: %s message: %s pins: %s" % (self.x, self.y, self.width, self.height, self.colour, self.message, self.pins)
   

while True:
    #print('The server is ready to receive')
    serverSocket.listen(1)
    
    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()
    #sentence = connectionSocket.recv(1024).decode()

    newthread = ClientThread(addr, connectionSocket)
    newthread.start()
    
serverSocket.close()  
sys.exit()
        
    

        
    

        
    
        
