import socket

# A simple server-client program
def Server():

    ''' 1. make a socket. '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))

    # reserve a port on your computer in our
    # case it is 12345 but it can be anything

    host = ''

    port = 12345     

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network 
    s.bind((host, port))  
    print ("socket binded to %s" %(port))

    # 5 here means that 5 connections are kept waiting if the server is busy and if a 6th socket tries to connect then the connection is refused.
    s.listen(5)
    print ("socket is listening")  

    # a forever loop until we interrupt it or
    # an error occurs
    while True:

        # Establish connection with client.
        ''' IMPORTANT: Why does accept () return a new socket c?
            Because the initial socket is used to wait for communication while the second is used to communicate'''
        
        c, addr = s.accept()    
        print ('Got connection from', addr)
        
        # send a thank you message to the client. encoding to send byte type.
        c.send('Thank you for connecting'.encode())
        
        # Close the connection with the client
        c.close()
        
        # Breaking once connection closed
        break

    s.close()

    '''
        1. First of all, we import socket which is necessary.

        2. Then we made a socket object and reserved a port on our pc.

        3. After that, we bound our server to the specified port. Passing an empty string means that the server can listen to incoming connections from other computers as well. 
        If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.

        4. After that we put the server into listening mode.5 here means that 5 connections are kept waiting if the server is busy and if a 6th socket tries to connect then the connection is refused.

        5. At last, we make a while loop and start to accept all incoming connections and close those connections after a thank you message to all connected sockets.

    '''

if __name__ == "__main__":

    Server()
