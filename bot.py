import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="/", status=discord.Status.online, activity=discord.Game(name="/help"))

@bot.command()
async def hello(ctx):
 await ctx.channel.send("Hello.")
 
@bot.command()
async def pipe(ctx):
 await ctx.channel.send("Yes pipe.")
 
@bot.command()
async def παρης(ctx):
 await ctx.channel.send("Ο Παρης ειναι μαλακας.")
 
 
@bot.command()
async def paris(ctx):
 await ctx.channel.send("Paris is an asshole.")
 
 
@bot.command()
async def wlu(ctx):
 testembed = discord.Embed(
   title = "What Lies Underneath",
   description = "What lies underneath server : https://discord.gg/cwerZuM.",
   colour = discord.Colour.blue()
 )
 
 testembed.set_author(name="Verifynow")
 testembed.set_footer(text="Wlu team")

 await ctx.channel.send(embed=testembed)
 
@bot.command()
async def verify(ctx):
 testembed = discord.Embed(
   title = "Verify bot",
   description = "Verify bot and site here : http://verifynow.cf/.",
   colour = discord.Colour.red()
 )
 
 testembed.set_author(name="Verifynow")
 testembed.set_footer(text="Wlu team")

 await ctx.channel.send(embed=testembed)


 
bot.run("NTc5MzU1NjEwMjY5NzQ1MTgz.XOA9Kw.meCipXhfSqDosWoRucfDY-LjnS0")
