''' Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.'''

'''They are the real backbones behind web browsing. In simpler terms, there is a server and a client. '''
'''Socket programming is started by importing the socket library and making a simple socket. '''

# https://www.geeksforgeeks.org/socket-programming-python/

import socket
import sys
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

''' Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_STREAM. '''

''' AF_INET refers to the address-family ipv4.'''
''' The SOCK_STREAM means connection-oriented TCP protocol. '''
''' Now we can connect to a server using this socket. '''

# find the IP of www.google.com using python
# ip = socket.gethostbyname('www.google.com')
# print (ip)

# Here is an example of a script for connecting to Google.
def Google_connection():

    ''' 1. make a socket. '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))
 
    # default port for socket
    port = 80

    ''' 2. get Google's host ip''' 
    try:
        host_ip = socket.gethostbyname("www.google.com")
    except socket.gaierror:

        # this means could not resolve the host
        print ("there was an error resolving the host")
        sys.exit()

    ''' 3. connecting to the server '''
    s.connect((host_ip, port))

    print ("the socket has successfully connected to google")

''' Client : 
    Now we need something with which a server can interact. We could telnet to the server like this just to know that our server is working. Type these commands in the terminal: 

    # start the server
    $ python server.py

    # keep the above terminal open 
    # now open another terminal and type: 
    
    $ telnet localhost 12345 '''

if __name__ == "__main__":

    Google_connection()



    







