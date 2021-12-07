[![Visistors](https://visitor-badge.glitch.me/badge?page_id=EterNomm.Chathon)](https://github.com/EterNomm/Chathon)
[![Downloads](https://static.pepy.tech/personalized-badge/chathon?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Total%20Downloads)](https://pepy.tech/project/chathon)
[![PyPI - Status](https://img.shields.io/pypi/status/chathon?label=Status&logo=python&logoColor=blue)](https://pypi.org/project/chathon)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/Chathon?label=PyPI%20Downloads&logo=pypi)](https://pypi.org/project/chathon)
[![PyPI](https://img.shields.io/pypi/v/chathon?label=PyPI%20Version&logo=pypi)](https://pypi.org/project/chathon)
[![GitHub issues](https://img.shields.io/github/issues/EterNomm/Chathon?label=Issues&logo=github)](https://github.com/EterNomm/Chathon/issues)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/y/EterNomm/Chathon?label=Commit%20Activity&logo=github)](https://github.com/EterNomm/Chathon/commits/main)
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

client = chathon.Client(username="LyQuid", badword_filter=True)
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
        <li>Using Decorator</li>
        <p>We will try to create a decorator for the bot command, for example: @bot.command()</p>
        <li>Bot can respond to users without prefix</li>
        <p>Example : user say "hello", then bot will respond "hi"</p>
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
