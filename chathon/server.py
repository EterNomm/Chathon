import socket
import threading
from time import sleep

class Server:
    r"""A class that implements the server side
    -----------
    Parameters :
    - ip: :class:`localhost/127.0.0.1` | you cannot change server ip because server ip always use localhost
    - port: :class:`int` | The server port.
    - record_conversation: :class:`False/True` | Record all client conversation in your server (if `True`, client will get warning message that your server is record all client conversation)
    """

    def __init__(self, port:int, record_conversation=False):
        host = '127.0.0.1'
        
        # Starting Server
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print("Server Online !")
        print()
        print("Server Information :")
        print(f"IP : {host} (use your network IP address for client connect to your server)")
        print(f"PORT : {port}")
        print(f"Print Client Message : {record_conversation}")
        print()
        self.print_log = record_conversation
        self.server = server

    def start(self):
        r"""Nothing, just function to start the server
        -----------
        """
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
                    if self.print_log == True:
                        message = str(message)
                        message = message.replace("'", "")
                        message = message.replace("b", "")
                        print(message)
                    else:
                        pass
                except:
                    # Removing And Closing Clients
                    index = clients.index(client)
                    clients.remove(client)
                    client.close()
                    nickname = nicknames[index]
                    broadcast('{} left!'.format(nickname).encode('UTF-8'))
                    print('{} left'.format(nickname))
                    nicknames.remove(nickname)
                    break
        
        def receive():
            while True:
                # Accept Connection
                client, address = server.accept()
                print("Connected with {}".format(str(address)))
        
                # Request And Store Nickname
                client.send('NICK'.encode('UTF-8'))
                nickname = client.recv(1024).decode('UTF-8')
                nicknames.append(nickname)
                clients.append(client)
        
                # Print And Broadcast Nickname
                print("New Client : {}".format(nickname))
                broadcast("{} joined!".format(nickname).encode('UTF-8'))
                client.send('Connected to server!'.encode('UTF-8'))
                if self.print_log == True:
                    client.send("\nWarning, the server may record your conversation.\n\n".encode('UTF-8'))
                else:
                    pass
        
                # Start Handling Thread For Client
                thread = threading.Thread(target=handle, args=(client,))
                thread.start()
            
        receive()
