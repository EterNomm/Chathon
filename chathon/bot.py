import socket
import threading
from time import sleep
import colorgb

class Bot:
    r"""A class that implements the bot engine.
    -----------
    Parameters :
    - bot_name: `str` | set bot username.
    - prefix: `str` | Bot prefix.
    - server_ip: `str` | Server IP for bot to enter.
    - server_port: `int` | Server Port for bot to enter.
    - bot_color: `str` | Set your bot username color. Scroll down to see the list of available colors.
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

    def __init__(self, bot_name:str, prefix:str, server_ip:str, server_port:int, bot_color:str=None):
        try:
           bot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           bot.connect((server_ip, server_port))
        except socket.error:
            print()
            print(colorgb.fore("An error occurred!", "lred"))
            print("Possible error(s) : Server offline, bot script error")
            print()
            bot.close()
            exit()
        
        if bot_color == None:
            self.bot_name = bot_name
        else:
            self.bot_name = colorgb.fore(bot_name, bot_color)
            
        self.prefix = prefix
        self.bot = bot
        self.user_input = None
        self.cache = {}
        self.response = None

    def command(self):
        """
        This method for bot command. Also, this method using Decorator.
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

    def run(self, debug=False):
        """
        A method to run the bot.
        ---
        Parameter :
        - debug: `True/False` | Is your bot for debugging/testing? if yes, then set `debug` to `True` (Default: `True`)
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
                    print()
                    print(colorgb.fore("An error occurred!", "lred"))
                    print("Possible error(s) : Server offline, bot script error")
                    print()
                    bot.close()
                    exit()

        def write():
            while True:
                prefix = self.prefix
                ui = self.user_input
                ui = str(ui)
                ui_replace = ui.split(": ")[1:]
                ui_replace = "".join(ui_replace)
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
                        if debug == True:
                            message = f"{nickname} {colorgb.fore('[DEBUG BOT]', 'lred')}: {self.response}"
                        else:
                            message = f"{nickname} {colorgb.fore('[BOT]', 'cyan')}: {self.response}"
                            
                        bot.send(message.encode('UTF-8'))
                        sleep(0.1) # prevent spam
                    else:
                        pass

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()
        write_thread = threading.Thread(target=write)
        write_thread.start()
