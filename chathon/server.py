import socket
import threading
from time import sleep
import colorgb

class Server:
    """A class that implements the server side.
    -----------
    Parameters :
    - ip: :class:`localhost/127.0.0.1` | you cannot change server ip because server ip always use localhost.
    - port: :class:`int` | The server port.
    - record_conversation: :class:`False/True` | Record all client conversation in your server (if `True`, client will get warning message that your server is record all client conversation).
    """

    def __init__(self, port:int, record_conversation=False):
        host = '127.0.0.1'
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen()
        print()
        print("Server Information :")
        print(f"Status : {colorgb.fore('Online', 'lgreen')}")
        print(f"IP : {host} (use your network IP address for client connect to your server)")
        print(f"PORT : {port}")
        if record_conversation == True:
            record_conversation = colorgb.fore(True, 'lred')
        else:
            record_conversation = colorgb.fore(True, 'lgreen')
        print(f"Record Conversation : {record_conversation}")
        print()
        self.print_log = record_conversation
        self.server = server
        self.welcome_msg = None

    def set_welcome_message(self, message:str):
        """
        Set welcome message when user join (Can only be seen by the user).
        -----
        Parameter :
        - message: `str`
        """
        message = f"{message}\n"
        self.welcome_msg = message
        print(f"Welcome message :")
        print(message)
        print()

    def start(self):
        """Nothing, just function to start the server.
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
                    message = client.recv(1024)
                    broadcast(message)
                    if self.print_log == True:
                        print(message.decode('UTF-8'))
                    else:
                        pass
                except:
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
                client, address = server.accept()
                print("Connected with {}".format(str(address)))
        
                client.send('NICK'.encode('UTF-8'))
                nickname = client.recv(1024).decode('UTF-8')
                nicknames.append(nickname)
                clients.append(client)
        
                print("New Client : {}".format(nickname))
                broadcast("{} joined!".format(nickname).encode('UTF-8'))
                if self.welcome_msg == None:
                    pass
                else:
                    client.send(self.welcome_msg.encode('UTF-8'))

                client.send('Connected to server!'.encode('UTF-8'))
                if self.print_log == True:
                    msg = colorgb.fore("Warning, the server may record your conversation.", "lred")
                    client.send(f"\n{msg}\n\n".encode('UTF-8'))
                else:
                    pass
        
                thread = threading.Thread(target=handle, args=(client,))
                thread.start()
            
        receive()
