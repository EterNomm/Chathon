import socket
import threading
import platform
import os
from better_profanity import profanity
import colorgb

class Client:
    r"""A class that implements the server side.
    -----------
    Parameters :
    - username: `str` | set your username to connect to server.
    - username_color: `str` | Set your username color. Scroll down to see the list of available colors. (Default: `None`)
    - badword_filter: `True/False` | Filter badword message. (Default : True)
    ----
    Basic Colors :
    - `black`
    - `red`
    - `green`
    - `yellow`
    - `blue`
    - `purple`
    - `cyan`
    - `white`
    -----
    Light Colors :
    - `grey`
    - `lred`
    - `lgreen`
    - `lyellow`
    - `lblue`
    - `lpurple`
    - `lcyan`
    """

    def __init__(self, username:str, username_color:str=None, badword_filter=True):
        if username_color == None:
            self.username = username
        else:
            self.username = f"{colorgb.fore(username, username_color)}"

        self.badword_filter = badword_filter

    def connect(self, server_ip:str, server_port:int):
        r"""Connect to the server
        -----------
        Parameters :
        - server_ip: :function:`str` | Server IP
        - server_port: :function:`int` | Server Port
        """

        nickname = self.username
        
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((server_ip, server_port))
        except socket.error:
            print()
            print(colorgb.fore("An error occurred!", "lred"))
            print("Possible error : Server offline.")
            print()
            client.close()
            exit()

        def receive():
            badword_filter = self.badword_filter
            while True:
                try:
                    message = client.recv(1024).decode('UTF-8')
                    if message == 'NICK':
                        client.send(nickname.encode('UTF-8'))
                    else:
                        if badword_filter == True:
                            censored = profanity.censor(message)
                            print(censored)
                        else:
                            print(message)
                except:
                    print()
                    print(colorgb.fore("An error occurred!", "lred"))
                    print("Possible error : Server offline.")
                    print()
                    client.close()
                    exit()

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
        
        receive_thread = threading.Thread(target=receive)
        receive_thread.start()
        
        write_thread = threading.Thread(target=write)
        write_thread.start()
