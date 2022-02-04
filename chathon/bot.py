import socket
import threading
from time import sleep

def listToStr(s): 
    string = " " 
    return (string.join(s))

class Bot:
    r"""A class that implements the bot engine.
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
        self.cache = {}
        self.response = None

    def command(self):
        """
        This method for bot command. This method using Decorator.
        Example : `@bot.command()`.
        See full example on github.
        """
        def decorator(func):
            self.cache[func.__name__] = func

        return decorator

    def send(self, message:str):
        """
        A method to send message when user use command.
        --
        Parameter :
        - message: `str`
        """
        self.response = message

    def run(self):
        """
        A method to run the bot.
        """

        bot = self.bot
        nickname = self.bot_name

        def receive():
            while True:
                try:
                    message = bot.recv(1024).decode('UTF-8')
                    if message == 'NICK':
                        bot.send(nickname.encode('UTF-8'))
                    else:
                        print(message)
                        self.user_input = message
                except:
                    print("An error occured!")
                    bot.close()
                    break

        def write():
            while True:
                prefix = self.prefix
                ui = self.user_input
                ui = str(ui)
                ui_replace = ui.split(": ")[1:]
                ui_replace = listToStr(ui_replace)
                arguments = ui_replace.split(" ")[1:]
                cmd_name = ui_replace.replace(prefix, "")
                cmd_name = cmd_name.split(" ")[0]
                get_input = ui_replace.split(" ")[0]

                command_name = self.cache.get(cmd_name)

                if command_name == None:
                    pass
                
                else:
                    if get_input == prefix+cmd_name:
                        command_name(*arguments)
                        message = '{}: {}'.format(f"{nickname} [BOT]", self.response)
                        bot.send(message.encode('UTF-8'))
                        sleep(1) # prevent spam
                    else:
                        pass

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()
        write_thread = threading.Thread(target=write)
        write_thread.start()
