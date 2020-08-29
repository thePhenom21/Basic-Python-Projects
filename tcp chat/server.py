import socket
import threading

host = '0.0.0.0'
port = 55555

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

clients = []
nicknames = []
#sending messagges to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

#handling messages from clients
def handle(client):
    while True:
        try:
            #Broadcasting message
            message = client.recv(1024)
            broadcast(message)
            if client not in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                nickname = nicknames[index]
                broadcast('{} left!'.format(nickname).encode('ascii'))
                
        except:
            #Removing and Closing Client Connections
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break        

def receive():
        #Request and store nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        print("Nickname is {}".format(nickname))

        broadcast("{} joined! ".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        #start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()    

def recei():
    global client
    while True:
        #Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        receive()

print("server is listening ...")
recei()


