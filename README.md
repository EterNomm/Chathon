# Chathon
A Python packages for make own chat room

## Install
- PyPI
```
pip install chathon
```
- Development version
```
pip install git+https://github.com/EterNomm/Chathon
```

## Examples

- Server side
```py
import chathon

server = chathon.Server(port=1212)
server.start()
```
- Client side
```py
import chathon

client = chathon.Client(username="LyQuid")
client.connect(server_ip="127.0.0.1", server_port=1212)
```
- Bot
```py
import chathon

bot = chathon.Bot(bot_name="Chathon", prefix="/", server_ip="127.0.0.1", server_port=1212)
bot.command(command_name="test", response="work!")
```

<details>
    <summary>Plan</summary>
    <br>
    <li>
        <a>Adding Colors</a>
        <p>This part will be done by <a href="https://github.com/TheGenocides" target="_blank">TheGenocides</a> using colorama</p>
    </li>
    <li>
        <a>Using Decorator</a>
        <p>We will try to create a decorator for the bot command, for example: @bot.command()</p>
    </li>
</details>

<details>
    <summary>Bug list</summary>
    <br>
    <li>
        <a>Spam (Small chances)</a>
        <p>Sometimes bots will spam when responding to users</p>
    </li>
</details>
