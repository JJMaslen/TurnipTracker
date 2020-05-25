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
import genericBot

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
    #dbMethods.createTable_weekPrices()
    #formatMethods.dayDeterminer()

@client.command()
async def test(ctx):
    now = datetime.now().strftime('%d-%m')
    print(now)

@client.command()
async def help(ctx):
    embed = discord.Embed(title='Bot Commands')
    embed.add_field(name = '!turnips', value = 'To see all current prices', inline = True)
    embed.add_field(name = '!myTurnips *num*', value = 'For updating your price', inline = True)
    embed.add_field(name = '!myWeek', value = 'To see your current week prices', inline = True)
    embed.add_field(name = '!myWeekHere', value = 'Shows your week prices in the current channel', inline = True)
    embed.add_field(name = '!addRole *role*', value = 'For adding a role to yourself', inline = True)
    embed.add_field(name = '!removeRole *role*', value = 'For removing a role from yourself', inline = True)
    await ctx.send(embed=embed)

@client.command()
async def turnips(ctx):

    formattedData = formatMethods.databaseConcatenaterTurnipTable()

    embed = discord.Embed(title='Turnip Prices')
    embed.add_field(name = 'Username', value = formattedData[0], inline = True)
    embed.add_field(name = 'Price', value = formattedData[1], inline = True)
    embed.add_field(name = 'Last Updated', value = formattedData[2], inline = True)

    channel = client.get_channel(694689627906506813)
    await channel.send(embed=embed)

    if ctx.message.channel.id != 694607433615540302:
        await ctx.message.delete()

@client.command()
async def myTurnips(ctx, newPrice):

    errorHandler = 0
    try:
        test = int(newPrice) + 1
        test = test - 1
        if test > 10 and test <= 660:
            errorHandler = 1
        else:
            await ctx.send("Please enter a whole number between 10 and 660 (Example: !myTurnips 100)")
    except:
        await ctx.send("Please enter a whole number between 10 and 660 (Example: !myTurnips 100)")

    if errorHandler == 1:
        userID = ctx.message.author.id
        userName = ctx.message.author.name
        now = datetime.now().strftime('%d-%m %H:%M')
        
        # Add user to Villager roleS
        await addRole(ctx, "Villager")

        # Check to see if user is in databases, and if not, add them
        dataTurnipTable = dbMethods.readTable_turnipTable()
        dataWeekPrices = dbMethods.readTable_weekPrices()
        inTurnipTable = False
        inWeekPricesTable = False
        for row in dataTurnipTable:
            if row[0] == userID:
                inTurnipTable = True
        
        for row in dataWeekPrices:
            if row[0] == userID:
                inWeekPricesTable = True

        if inTurnipTable == False:
            await ctx.send("You're not in my database, I'm adding you now!")
            dbMethods.addEntry_turnipTable(userID, userName, newPrice, now)
        
        if inWeekPricesTable == False:
            dbMethods.addEntry_weekPrices(userID, userName)

        # Update the users price
        await ctx.send("Updating your price now!")
        dbMethods.updateEntry_turnipTable(userID, newPrice, now)
        dbMethods.updateEntry_weekPrices(userID, newPrice)
        await ctx.send("Your new price is: {}".format(newPrice))


        # Tell users of price if price is high
        notif = genericBot.PriceCheck(int(newPrice))
        user = ctx.message.author
        roleList = user.guild.roles

        if notif == 0:
            role = genericBot.searchRoles(roleList, "LF-Low")
            mentions = role.mention
        elif notif == 1:
            role = genericBot.searchRoles(roleList, "LF-Low")
            mentions = role.mention
            role = genericBot.searchRoles(roleList, "LF-Mid")
            mentions += role.mention
        elif notif == 2:
            role = genericBot.searchRoles(roleList, "LF-Low")
            mentions = role.mention
            role = genericBot.searchRoles(roleList, "LF-Mid")
            mentions += role.mention
            role = genericBot.searchRoles(roleList, "LF-High")
            mentions += role.mention
        
        try:
            await ctx.send(mentions)
        except:
            pass

        await turnips(ctx)

@client.command()
async def myWeek(ctx):
    user = ctx.message.author
    userID = ctx.message.author.id
    weekPrices = formatMethods.databaseConcatenaterWeekPrices(userID)

    await user.send(weekPrices)

@client.command()
async def myWeekHere(ctx):
    userID = ctx.message.author.id
    weekPrices = formatMethods.databaseConcatenaterWeekPrices(userID)

    await ctx.send(weekPrices)

@client.command()
async def addRole(ctx, role):
    user = ctx.message.author
    roleList = user.guild.roles

    newRole = genericBot.searchRoles(roleList, role)
    if newRole != None:
        if newRole not in user.roles:
            await user.add_roles(newRole)
            await ctx.send("Enjoy your new role!")
    else:
        await ctx.send("That isn't a role! Current roles you can have are: Villager, LF-Low, LF-Mid, LF-High")

@client.command()
async def removeRole(ctx, role):
    user = ctx.message.author
    roleList = user.guild.roles

    newRole = genericBot.searchRoles(roleList, role)

    if newRole != None:
        await user.remove_roles(newRole)
        await ctx.send("Role has been removed")
    else:
        await ctx.send("That isn't a role! Current roles you can have are: Villager, LF-Low, LF-Mid, LF-High")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    stockTicker = 694689627906506813
    if message.channel.id == stockTicker:
        await message.delete(delay=5.0)

    await client.process_commands(message)

file = open("token.txt", "r")
token = str(file.read())
file.close()
client.run(token)