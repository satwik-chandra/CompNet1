# Import socket module
import socket 
from random import randint            
MESSAGE_HEADER = "Client"      

DISCONNECT_MESSAGE = "DISCONNECT" 
# Create a socket object
s = socket.socket()        
temprature = randint(25,60)
temprature_msg = f"Sensor 2 Reading: {temprature}" 
temprature_msg = MESSAGE_HEADER + temprature_msg 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.send(temprature_msg.encode())
s.close()    
     