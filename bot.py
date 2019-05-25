import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="?", status=discord.Status.online, activity=discord.Game(name="Made by filegeiasou#0935"))
   
@bot.event
async def on_ready():
 print(f"{bot.user.name} is ready")
 await bot.change_presence(activity=discord.Game(name="Made by filegeiasou#0935"))
                                            
 
@bot.event
async def on_member_join(member):
 channel = discord.utils.get(member.guild.channels, name="welcome")
 await channel.send(f"Welcome to the server{member.mention}😀")
 role = discord.utils.get(member.guild.roles, name="Member")
 await member.send("Welcome to the server.Write ?help to see the commands about bot.Made by filegeiasou#0935")
 await member.add_roles(role)
   
@bot.command()
async def info(ctx):
 await ctx.author.send("https://www.youtube.com/watch?v=6rpereSDELs")


@bot.command()
async def clear(ctx, amount: int):
 admins = ["filegeiasou#0935"]
 if str(ctx.message.author) in admins:  
  await ctx.channel.purge(limit=amount)
  await ctx.channel.send(f"Cleared {amount} messages.")
 else:
  await ctx.channel.send("You do not have permission to use this command.")
  
@bot.command()
async def kick(ctx, user: discord.User = None):
 admins = ["filegeiasou#0935"]
 if str(ctx.message.author) in admins:
  await ctx.guild.kick(user)
  await ctx.channel.send(f"I kicked {user}!")
 else:
  await ctx.channel.send("You do not have permission to use this command.")
    
@bot.command()
async def hello(ctx):
 await ctx.channel.send("Hello.")
 
 
@bot.command()
async def wlu(ctx):
 testembed = discord.Embed(
   title = "What Lies Underneath",
   description = "What lies underneath server : https://discord.gg/cwerZuM. What lies underneath site : https://whatliesunderneath.cf/.",
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
  colour = discord.Colour.yellow()
 )
 
 testembed.set_author(name="Verifynow")
 testembed.set_footer(text="Wlu team")

 await ctx.channel.send(embed=testembed)

@bot.command()
async def site(ctx):
 testembed = discord.Embed(
   title = "Verify bot",
   description = "Everyone who wants to help with bot send email here : http://verifynow.cf/.",
   colour = discord.Colour.purple()
 )
 
 testembed.set_author(name="Verifynow")
 testembed.set_footer(text="Wlu team")

 await ctx.channel.send(embed=testembed)
 
bot.run("NTc5MzU1NjEwMjY5NzQ1MTgz.XOA9Kw.meCipXhfSqDosWoRucfDY-LjnS0")
