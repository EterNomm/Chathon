[![Visistors](https://visitor-badge.glitch.me/badge?page_id=EterNomm.Chathon)](https://github.com/EterNomm/Chathon)
[![PyPI - Status](https://img.shields.io/pypi/status/chathon?label=Status&logo=python&logoColor=blue)](https://pypi.org/project/chathon)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/Chathon?label=PyPI%20Downloads&logo=pypi)](https://pypi.org/project/chathon)
[![PyPI](https://img.shields.io/pypi/v/chathon?label=PyPI%20Version&logo=pypi)](https://pypi.org/project/chathon)
[![GitHub stars](https://img.shields.io/github/stars/EterNomm/Chathon?label=Stars&logo=github)](https://github.com/EterNomm/Chathon/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/EterNomm/Chathon?label=Forks&logo=github)](https://github.com/EterNomm/Chathon/network)
[![GitHub issues](https://img.shields.io/github/issues/EterNomm/Chathon?label=Issues&logo=github)](https://github.com/EterNomm/Chathon/issues)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/EterNomm/Chathon?label=Commit%20Activity&logo=github)
[![Discord](https://img.shields.io/discord/887650006977347594?color=blue&label=EterNomm&logo=discord&logoColor=blue)](https://discord.com/invite/qpT2AeYZRN)

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

server = chathon.Server(port=1212, record_conversation=False)
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
    <ul>
        <li>Adding Colors</li>
        <p>This part will be done by <a href="https://github.com/TheGenocides" target="_blank">TheGenocides</a> using colorama</p>
        <li>Using Decorator</li>
        <p>We will try to create a decorator for the bot command, for example: @bot.command()</p>
    </ul>
</details>

<details>
    <summary>Bug list</summary>
    <br>
    <ul>
        <li>Spam (Small chances)</li>
        <p>Sometimes bots will spam when responding to users</p>
    </ul>
</details>
