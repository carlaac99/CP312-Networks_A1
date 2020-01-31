'''
Created on Jan. 28, 2020

@author: nicolelaslavic
'''
# Import socket module
from socket import * 
import sys # In order to terminate the program

serverName = 'localhost'
# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
print("1-connect \n2-disconnect \n3-POST \n4-GET \n5-PIN \n6-UNPIN \n7-CLEAR\n")
option = input("Enter menu option: ")

while(option<'8' and option>'0'):
    if option == '1':
        user_input = 'CONNECT'
    elif option == '2':
        user_input = 'DISCONNECT'
    elif option == '3':
        user_input = input("Enter POST: ")
        user_input = 'POST '+ user_input
    elif option == '4':
        user_input = '4'
        user_input = 'GET '+ user_input
    elif option == '5':
        user_input = input("Enter PIN: ")
        user_input = 'PIN '+ user_input
    elif option == '6':
        user_input = input("Enter UNPIN: ")
        user_input = 'UNPIN '+ user_input
    elif option == '7':
        user_input = 'CLEAR'
    else:
        print("Invalid menu option.")
    
    clientSocket. sendall(user_input.encode())
    print("encoded")
    modifiedSentence = clientSocket.recv(2048)
    print("recv")
    print('From server: ', (modifiedSentence).decode())
    print("decoded")
        
    print("1-connect \n2-disconnect \n3-POST \n4-GET \n5-PIN \n6-UNPIN \n7-CLEAR")
    option = input("Enter menu option: ")

#sentence = input(' Input lower case sentence: ')
#clientSocket. sendall(user_input.encode())

clientSocket.close()
