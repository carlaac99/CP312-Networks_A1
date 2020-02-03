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
# clientSocket.connect((serverName, serverPort))

print("1-connect \n8-EXIT ")
option =0

while (option!=8):
    try:
        option = int(input("Enter menu option number: "))
        if(option==1 or option==8):
            break
        else:
            print("\nyou need to connect first to continue to options, or exit if you wish to exit the program.")
    except ValueError:
        print("you did not enter a valid number. Try again, or type the number 8 to exit the program.")
        

while(True):
    
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
        print("input: <x-coordinate y-coordinate width height colour message>")
        user_input = input("Enter POST: ")
        if(user_input == ""):
            print("This method requires user input.")
            user_input = "!"
        else:
            user_input = 'POST '+ user_input
    elif option == 4:
        print("options: \npins (all pinned notes) \ncontains= <x-coordinate y-coordinate> \nrefersTo= <string> \ncolour= <colour string> \ncolour= <empty> (all on board)")
        user_input = input("Enter GET: ")
        if(user_input == ""):
            print("This method requires user input.")
            user_input = "!"
        else:
            user_input = 'GET '+ user_input
    elif option == 5:
        print("input: x-coordinate y-coordinate")
        user_input = input("Enter PIN: ")
        user_input = 'PIN '+ user_input
    elif option == 6:
        print("input: x-coordinate y-coordinate")
        user_input = input("Enter UNPIN: ")
        user_input = 'UNPIN '+ user_input
    elif option ==7:
        user_input = 'CLEAR'

 
    else:
        print("\ninvalid menu option please enter the numbers in the menu.")


    if (option<8 and option>0):

        clientSocket. sendall(user_input.encode())

        if (option==2):
            print("you have been disconnected")
            break
              
        modifiedSentence = clientSocket.recv(2048)

        print('From server: ', (modifiedSentence).decode())

#              
          
    print("\n1-connect \n2-disconnect \n3-POST \n4-GET \n5-PIN \n6-UNPIN \n7-CLEAR \n8-EXIT")
    
        
    while (True):
        try:
            option = int(input("Enter menu option number: "))
            break
        except ValueError:
            print("invalid menu option please enter the numbers in the menu..")
#sentence = input(' Input lower case sentence: ')
#clientSocket. sendall(user_input.encode())

clientSocket.close()

