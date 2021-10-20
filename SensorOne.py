# Import socket module
import socket
from random import randint            
DISCONNECT_MESSAGE = "DISCONNECT" 
# Create a socket object
s = socket.socket()        
temprature = randint(25,60) 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.send((f"*******The temprature is {temprature} degree Celcius**FROM SENSOR 1*****").encode())
s.close()    
     