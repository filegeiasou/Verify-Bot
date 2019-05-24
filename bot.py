import discord
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="?", status=discord.Status.online, activity=discord.Game(name="Made by filegeiasou#0935"))


bot.command(‘guildMemberAdd’, member => {
  member.send(`Welcome on the server! Please be aware that we won’t tolerate troll, spam or harassment. Have fun 😀`)
})

@bot.command()
async def clear(ctx, amount: int):
 admins = ["filegeiasou#0935"]
 if str(ctx.message.author) in admins:  
  await ctx.channel.purge(limit=amount)
  await ctx.channel.send(f"Cleared {amount} messages.")
  
  
  
@bot.command()
async def kick(ctx, user: discord.User = None):
 await ctx.guild.kick(user)
 await ctx.channel.send(f"I kicked {user}!")
    
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
   colour = discord.Colour.red()
 )
 
 testembed.set_author(name="Verifynow")
 testembed.set_footer(text="Wlu team")

 await ctx.channel.send(embed=testembed)

@bot.command()
async def test(ctx):
 testembed = discord.Embed(
   title = "Verify bot",
   description = "Everyone who wants to help with bot send email here : http://verifynow.cf/.",
   colour = discord.Colour.purple()
 )
 
 testembed.set_author(name="Verifynow")
 testembed.set_footer(text="Wlu team")

 await ctx.channel.send(embed=testembed)
 
bot.run("NTc5MzU1NjEwMjY5NzQ1MTgz.XOA9Kw.meCipXhfSqDosWoRucfDY-LjnS0")
