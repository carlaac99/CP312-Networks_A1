'''
Created on Jan. 28, 2020
@author: carla castaneda
'''
# Import socket module
from socket import * 
import sys # In order to terminate the program

serverName = 'localhost'
# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)


print("1-connect \n8-EXIT ")
option =0

while (option!=9):
    try:
        option = int(input("Enter menu option number: "))
        if(option==1 or option==9):
            break
        else:
            print("you must type '1 'to connect first.")
    except ValueError:
        print("you did not enter a valid number. Try again, or type the number 8 to exit the program.")
        
connection=False
while(option<8 and option> 0):
    
    user_input=""
    if option == 1  :
        user_input = 'CONNECT'
        try:
            clientSocket.connect((serverName, serverPort))
        except OSError as e:
            print(e)
        
    elif option == 2:
        user_input = 'DISCONNECT'
        
    elif option == 3:
        user_input = input("Enter POST: ")
        user_input = 'POST '+ user_input
    elif option == 4:
        user_input = input("Enter GET: ")
        user_input = 'GET '+ user_input
    elif option == 5:
        user_input = input("Enter PIN: ")
        user_input = 'PIN '+ user_input
    elif option == 6:
        user_input = input("Enter UNPIN: ")
        user_input = 'UNPIN '+ user_input
    elif option ==7:
        user_input = 'CLEAR'

    else:
        print("Invalid menu option.")

    if (option<8 and option>1):
        clientSocket. sendall(user_input.encode())
        print("encoded")
        
        modifiedSentence = clientSocket.recv(2048)
        print("recv")
        print('From server: ', (modifiedSentence).decode())
        print("decoded")
        
        
    print("\n1-connect \n2-disconnect \n3-POST \n4-GET \n5-PIN \n6-UNPIN \n7-CLEAR \n8-EXIT")
    
        
    while (True):
        try:
            option = int(input("Enter menu option number: "))
            break
        except ValueError:
            print("you did not enter a valid number.")
#sentence = input(' Input lower case sentence: ')
#clientSocket. sendall(user_input.encode())

clientSocket.close()
