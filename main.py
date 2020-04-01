# Main Imports
from datetime import datetime

# Discord Imports
import discord
import discord.ext
from discord.ext.commands import Bot
from discord.ext import commands

# Local File Imports
import dbMethods
import formatMethods

bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command("help")

@client.event
async def on_ready():
    print("Turnip Tracker is online!")
    print("Name: Turnip Tracker")
    print("TD: {}".format(client.user.id))
    #dbMethods.createTable()
    #dbMethods.editTable()

@client.command()
async def test(ctx):
    #await ctx.send("Hello, this is a test!")
    #userID = ctx.message.author.id
    #userName = ctx.message.author.name
    #await ctx.send("Thank you {} , id: {}".format(userName,userID))
    #now = datetime.now().strftime('%d-%m %H:%M')
    #await ctx.send("The current time is: {}".format(now))
    pass

@client.command()
async def help(ctx):
    embed = discord.Embed(title='Bot Commands')
    embed.add_field(name = '!turnips', value = 'For current prices', inline = True)
    embed.add_field(name = '!myTurnips *num*', value = 'For updating your price', inline = True)

    await ctx.send(embed=embed)

@client.command()
async def turnips(ctx):

    formattedData = formatMethods.databaseConcatenater()
    
    embed = discord.Embed(title='Turnip Prices')
    embed.add_field(name = 'Username', value = formattedData[0], inline = True)
    embed.add_field(name = 'Price', value = formattedData[1], inline = True)
    embed.add_field(name = 'Last Updated', value = formattedData[2], inline = True)

    await ctx.send(embed=embed)

@client.command()
async def myTurnips(ctx, newPrice):

    errorHandler = 0
    try:
        test = int(newPrice) + 1
        test = test - 1
        if test > 1 and test <= 999:
            errorHandler = 1
        else:
            await ctx.send("Please enter a whole number between 1 and 999 (Example: !myTurnips 100)")
    except:
        await ctx.send("Please enter a whole number between 1 and 999 (Example: !myTurnips 100)")

    if errorHandler == 1:
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