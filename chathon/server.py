import socket
import threading

class Server:
    def __init__(self, port):
        host = '127.0.0.1'
        
        # Starting Server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print("Server Online !")
        self.server = server

    def start(self):
        clients = []
        nicknames = []
        server = self.server
        
        def broadcast(message):
            for client in clients:
                client.send(message)
        
        def handle(client):
            while True:
                try:
                    # Broadcasting Messages
                    message = client.recv(1024)
                    broadcast(message)
                except:
                    # Removing And Closing Clients
                    index = clients.index(client)
                    clients.remove(client)
                    client.close()
                    nickname = nicknames[index]
                    broadcast('{} left!'.format(nickname).encode('ascii'))
                    print('{} left'.format(nickname))
                    nicknames.remove(nickname)
                    break
        
        def receive():
            while True:
                # Accept Connection
                client, address = server.accept()
                print("Connected with {}".format(str(address)))
        
                # Request And Store Nickname
                client.send('NICK'.encode('ascii'))
                nickname = client.recv(1024).decode('ascii')
                nicknames.append(nickname)
                clients.append(client)
        
                # Print And Broadcast Nickname
                print("New Client : {}".format(nickname))
                broadcast("{} joined!".format(nickname).encode('ascii'))
                client.send('Connected to server!'.encode('ascii'))
        
                # Start Handling Thread For Client
                thread = threading.Thread(target=handle, args=(client,))
                thread.start()
            
        receive()
