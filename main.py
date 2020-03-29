# Main Imports
from datetime import datetime

# Discord Imports
import discord
import discord.ext
from discord.ext.commands import Bot
from discord.ext import commands

# Local File Imports
import dbMethods

bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

@client.event
async def on_ready():
    print("Turnip Tracker is online!")
    print("Name: Turnip Tracker")
    print("TD: {}".format(client.user.id))
    dbMethods.setUp()

@client.command()
async def test(ctx):
    await ctx.send("Hello, this is a test!")
    userID = ctx.message.author.id
    userName = ctx.message.author.name
    await ctx.send("Thank you {} , id: {}".format(userName,userID))
    now = datetime.now().strftime('%d-%m %H:%M')
    await ctx.send("The current time is: {}".format(now))

@client.command()
async def Turnips(ctx):
    pass

@client.command()
async def myTurnips(ctx):
    pass

file = open("token.txt", "r")
token = str(file.read())
file.close()
client.run(token)