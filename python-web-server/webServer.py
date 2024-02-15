# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    
    #print('Ready to serve...')
    connectionSocket, addr = addr = serverSocket.accept() #Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode() #Fill in start -a client is sending you a message   #Fill in end 
      #print(message +"\n")
      filename = message.split()[1]
      
      #print("How I split it\n")
      #print(filename[1:])
      #print("\n")
      #opens the client requested file. 
      #Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
      f = open(filename[1:], "r")#fill in start #fill in end)
      #fill in end
      

      #This variable can store the headers you want to send for any valid or invalid request.   What header should be sent for a response that is ok?    
      #Fill in start 
              
      #Content-Type is an example on how to send a header as bytes. There are more!
      outputdata = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nServer: Apache/2.2.14 (Win32)\r\nConnection: keep-alive\r\n\r\n"


      #Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n" Refer to https://w3.cs.jmu.edu/kirkpams/OpenCSF/Books/csf/html/TCPSockets.html
 
      #Fill in end

      for i in f: #for line in file
        outputdata+=i.encode('utf-8')

      #Fill in start - append your html file contents #Fill in end 
        
      #Send the content of the requested file to the client (don't forget the headers you created)!
      # Fill in start
      connectionSocket.send(outputdata)

      # Fill in end
        
      connectionSocket.close() #closing the connection socket
      
    except Exception as e:
      # pass
      # Send response message for invalid request due to the file not being found (404)
      # Remember the format you used in the try: block!
      #Fill in start
      outputdata = b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\nServer: Apache/2.2.14 (Win32)\r\nConnection: close\r\n\r\n"
      connectionSocket.send(outputdata)
      #Fill in end


      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)