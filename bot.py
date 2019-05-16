import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="-", status=discord.Status.idle, activity=discord.Game(name="With your mom..."))

@bot.command()
async def verify(ctx):
 await ctx.channel.send("Hello.")
 
@bot.command()
async def pipe(ctx):
 await ctx.channel.send("Yes pipe.")
 
@bot.command()
async def παρης(ctx):
 await ctx.channel.send("Ο Παρης ειναι μαλακας.")
 
@bot.command()

async def site(ctx):

 await ctx.channel.send(" To verify here : http://verifynow.cf/")
 
@bot.command()
async def paris(ctx):
 await ctx.channel.send("Paris is an asshole.")
 
@bot.command()

async def wlu(ctx):

 await ctx.channel.send("What lies underneath server : https://discord.gg/yCaRxp.")
   
 
bot.run("NTc3NTQyMzM2MTE3MjExMTQ2.XNmmTg.hpekKwefCTL6FOr9LllnDySJ5gY")
