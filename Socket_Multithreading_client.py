import socket

def Client():

    # local host IP '127.0.0.1'
    host = '127.0.0.1'
 
    # Define the port on which you want to connect
    port = 12345

    ''' make a socket. '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))

    # connect to server on local computer
    s.connect((host,port))

    # message you send to server
    message = "shaurya says geeksforgeeks"

    while True:

        # message sent to server
        s.send(message.encode("ascii"))

        # message received from server
        data = s.recv(1024)

        # print the received message
        # here it would be a reverse of sent message
        print('Received from the server :', str(data.decode('ascii')))

        ans = input('\nDo you want to continue(y/n) :')
        if ans == "y":
            continue
        else:
            break

        # close connection
        s.close()

    if __name__ == "__main__":

        Client()