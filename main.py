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
    dbMethods.createTable()

@client.command()
async def test(ctx):
    await ctx.send("Hello, this is a test!")
    userID = ctx.message.author.id
    userName = ctx.message.author.name
    await ctx.send("Thank you {} , id: {}".format(userName,userID))
    now = datetime.now().strftime('%d-%m %H:%M')
    await ctx.send("The current time is: {}".format(now))

@client.command()
async def turnips(ctx):
    data = dbMethods.readTable()

    embed = discord.Embed(title='Turnip Prices')
    for row in data:
        embed.add_field(name = 'Username', value = row[1], inline = True)
        embed.add_field(name = 'Price', value = row[2], inline = True)
        embed.add_field(name = 'Last Updated', value = row[3], inline = True)

    await ctx.send(embed=embed)

@client.command()
async def myTurnips(ctx, newPrice):
    userID = ctx.message.author.id
    userName = ctx.message.author.name
    now = datetime.now().strftime('%d-%m %H:%M')

    data = dbMethods.readTable()
    inDatabase = False
    for row in data:
        if row[0] == userID:
            inDatabase = True
            
    if inDatabase == False:
        await ctx.send("You're not in my database, I'm adding you now!")
        dbMethods.addEntry(userID, userName, newPrice, now)

    await ctx.send("Updating your price now!")
    dbMethods.updateEntry(userID, newPrice, now)

    await ctx.send("Your new price is: {}".format(newPrice))

file = open("token.txt", "r")
token = str(file.read())
file.close()
client.run(token)