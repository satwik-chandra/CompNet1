# Import socket module
import socket    
import pickle        
DISCONNECT_MESSAGE = "DISCONNECT"
ASK_REQUEST = "SEND TEMPS" 
# Create a socket object
s = socket.socket()        
 
# Define the port on which you want to connect
port = 12345               
 
# connect to the server on local computer
s.connect(('127.0.0.1', port))
 
# receive data from the server and decoding to get the string.
print (s.recv(1024).decode())
# close the connection
s.send(ASK_REQUEST.encode())

pickled_message = s.recv(1024)
messages = pickle.loads(pickled_message)

for msg in messages:
    print(msg + "\n")

s.close()    
     