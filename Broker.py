import socket  
import pickle          
 
# next create a socket object
s = socket.socket() 
       
print ("Socket successfully created")
messages = []
DISCONNECT_MESSAGE = "DISCONNECT" 
TERMINATE_MESSAGE = "TERMINATE" 
ASK_REQUEST = "SEND TEMPS"
CLIENT_MESSAGE_HEADER = "Client"
SERVER_MESSAGE_HEADER = "Server" 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
PORT_CLIENTS = 12345   
           
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('', PORT_CLIENTS))        
print ("socket binded to %s" %(PORT_CLIENTS))
# put the socket into listening mode
s.listen(4)    
print ("Server socket is listening")
           
 
# a forever loop until we interrupt it or
# an error occurs
while True:
 
# Establish connection with client.
  c, addr = s.accept()   
  print ('Got connection from', addr )
 
  # send a thank you message to the client. encoding to send byte type.
  c.send('Thank you for connecting'.encode())
  print ()
  # Close the connection with the client
  msg = c.recv(1024).decode()   
  if msg == DISCONNECT_MESSAGE:
      c.close()
  elif msg == ASK_REQUEST:
      print("Sending info to the dashboard")
      pickled_SERVER_Header = pickle.dumps(SERVER_MESSAGE_HEADER)
      pickled_messages = pickle.dumps(messages)
      pickled_messages = pickled_SERVER_Header + pickled_messages
      c.send(pickled_messages)
  elif msg[0:6] == CLIENT_MESSAGE_HEADER:
      messages.append(msg[6:])
      print("Message recieved from Sensor \n")



