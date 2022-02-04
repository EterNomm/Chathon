import chathon

bot = chathon.Bot(bot_name="Chathon", prefix="/", server_ip="127.0.0.1", server_port=1212)

@bot.command()
def hi():
    bot.send("Hi !")

@bot.command()
def sum(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    bot.send(num1+num2)

@bot.command()
def echo(*a):   # Add * before parameter to print all user argument
    a = "".join(a) # Use this to convert tuple to string
    bot.send(a)

bot.run()
