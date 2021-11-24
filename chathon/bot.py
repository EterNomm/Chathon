import socket
import threading
from time import sleep

class Bot:
    r"""A class that implements the bot engine
    -----------
    Parameters :
    - bot_name: :class:`str` | set bot username
    - prefix: :class:`str` | Bot prefix
    - server_ip: :class:`str` | Server IP for bot to enter
    - server_port: :class:`int` | Server Port for bot to enter
    """

    def __init__(self, bot_name:str, prefix:str, server_ip:str, server_port:int):
        bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bot.connect((server_ip, server_port))

        self.bot_name = bot_name
        self.prefix = prefix
        self.bot = bot
        self.user_input = None

    def command(self, command_name, response):
        r"""A class that implements the bot engine
        -----------
        Parameters :
        - command_name: :class:`str` | command name so that clients can use it, for example: `test` for`/test`
        - response: :class:`str` | Command response
        """

        bot = self.bot
        nickname = self.bot_name
        prefix = self.prefix
        def receive():
            while True:
                try:
                    # Receive Message From Server
                    # If 'NICK' Send Nickname
                    message = bot.recv(1024).decode('UTF-8')
                    if message == 'NICK':
                        bot.send(nickname.encode('UTF-8'))
                    else:
                        print(message)
                        user_msg = message
                        get_cmd = str(user_msg.split(" ")[1:])
                        get_cmd = get_cmd.replace("[", "")
                        get_cmd = get_cmd.replace("]", "")
                        get_cmd = get_cmd.replace("'", "")
                        self.user_input = get_cmd
                except:
                    # Close Connection When Error
                    print("An error occured!")
                    bot.close()
                    break

        def write():
            while True:
                if self.user_input == f"{prefix}{command_name}":
                    message = '{}: {}'.format(f"{nickname} [BOT]", response)
                    bot.send(message.encode('UTF-8'))
                    sleep(1) # prevent spam
                else:
                    pass

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()
        write_thread = threading.Thread(target=write)
        write_thread.start()
