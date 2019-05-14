import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="/", status=discord.Status.idle, activity=discord.Game(name="Testing.."))

@bot.command()
async def verify(ctx):
 await ctx.channel.send("Hello.")
 
bot.run("NTc3NTQyMzM2MTE3MjExMTQ2.XNmmTg.hpekKwefCTL6FOr9LllnDySJ5gY")
