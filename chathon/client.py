import socket
import threading
import platform
import os

class Client:
    r"""A class that implements the server side
    -----------
    Parameters :
    - username: :class:`str` | set your username to connect to server
    """

    def __init__(self, username:str):
        self.username = username

    def connect(self, server_ip:str, server_port:int):
        r"""Connect to the server
        -----------
        Parameters :
        - server_ip: :function:`str` | Server IP
        - server_port: :function:`int` | Server Port
        """

        nickname = self.username
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, server_port))

        def receive():
            while True:
                try:
                    # Receive Message From Server
                    # If 'NICK' Send Nickname
                    message = client.recv(1024).decode('UTF-8')
                    if message == 'NICK':
                        client.send(nickname.encode('UTF-8'))
                    else:
                        print(message)
                except:
                    # Close Connection When Error
                    print("An error occured!")
                    client.close()
                    break

        def write():
            while True:
                input_msg = input('')
                if input_msg == "/clear":
                    if platform.uname()[0] == "Windows":
                        os.system("cls")
                    else:
                        os.system("clear")

                else:
                    message = '{}: {}'.format(nickname, input_msg)
                    client.send(message.encode('UTF-8'))
        
        # Starting Threads For Listening And Writing
        receive_thread = threading.Thread(target=receive)
        receive_thread.start()
        
        write_thread = threading.Thread(target=write)
        write_thread.start()
