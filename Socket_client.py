import socket

''' Client : 
    Now we need something with which a server can interact. We could telnet to the server like this just to know that our server is working. Type these commands in the terminal: 

    # start the server
    $ python server.py

    # keep the above terminal open 
    # now open another terminal and type: 
 
    $ telnet localhost 12345
    If ‘telnet’ is not recognized. On windows search windows features and turn on the “telnet client” feature. '''

def Client():
    
    # Create a socket object
    s = socket.socket()        
    
    # Define the port on which you want to connect
    port = 12345               
    
    # connect to the server on local computer
    s.connect(('127.0.0.1', port))
    
    # receive data from the server and decoding to get the string.
    data = s.recv(1024).decode()

    print(data)
    
    # close the connection
    s.close()    

    " 1. First of all, we make a socket object."
    " 2. Then we connect to localhost on port 12345 (the port on which our server runs) and lastly, we receive data from the server and close the connection. "
    " 3. Now save this file as client.py and run it from the terminal after starting the server script."

if __name__ == "__main__":

    Client()