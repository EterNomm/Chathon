import socket
import threading
import platform
import os

class Client:
    def __init__(self, username:str):
        self.username = username

    def connect(self, server_ip:str, server_port:int):
        nickname = self.username
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server_ip, server_port))

        def receive():
            while True:
                try:
                    # Receive Message From Server
                    # If 'NICK' Send Nickname
                    message = client.recv(1024).decode('ascii')
                    if message == 'NICK':
                        client.send(nickname.encode('ascii'))
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
                    client.send(message.encode('ascii'))
        
        # Starting Threads For Listening And Writing
        receive_thread = threading.Thread(target=receive)
        receive_thread.start()
        
        write_thread = threading.Thread(target=write)
        write_thread.start()
