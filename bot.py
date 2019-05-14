import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="/", status=discord.Status.idle, activity=discord.Game(name="With your mum..."))

@bot.command()
async def verify(ctx):
 await ctx.channel.send("Hello.")
 
@bot.command()
async def pipe(ctx):
 await ctx.channel.send("Yes pipe.")
if (ctx==pipe):
  print("https://discordapp.com/api/oauth2/authorize?client_id=577542336117211146&permissions=0&scope=bot"
else:
  print("Pipe")
       
 
bot.run("NTc3NTQyMzM2MTE3MjExMTQ2.XNmmTg.hpekKwefCTL6FOr9LllnDySJ5gY")
