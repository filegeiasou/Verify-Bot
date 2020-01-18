import discord
import asyncio
import random
import os
import sys
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from itertools import cycle

status = cycle([ "Made by filegeiasou", "write a!help" ])
bot = commands.Bot(command_prefix="a!", status=discord.Status.online, activity=discord.Game(name="Made by filegeiasou#0935"))

bot.remove_command('help')
@bot.event
async def on_ready():
    change_status.start()
    print(f"{bot.user.name} is ready")
    await bot.change_presence(activity=discord.Game(name="Made by filegeiasou#0935"))

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await member.send(f"Welcome {member.mention} to our server")
    role = discord.utils.get(member.guild.roles, name="Members")
    await member.add_roles(role)

@tasks.loop(seconds=8)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))



@bot.command()
async def avatar(ctx, user: discord.User = None):
 embed = discord.Embed(
  title = "Verify Bot",
  description = "Avatar",
  colour = discord.Colour.dark_blue()
 )

 pfp = user.avatar_url

 embed.set_footer(text="Made by filegeiasou#0935")
 embed.set_image(url=pfp)
 await ctx.channel.send(embed=embed)

@bot.command()
async def profile(ctx, member: discord.Member):
    embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)
    embed.add_field(name="Created at:", value=member.created_at.strftime("%a , %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a , %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Top role:", value=member.top_role.mention)

    await ctx.send(embed=embed)




@bot.command()
async def info(ctx):
    await ctx.author.send("Do you like to help me with command send me email here: filegeiasou@gmail.com.")



@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
        await ctx.channel.purge(limit=amount)



@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    
    
    
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned{member.mention}')


@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    
    for ban_entry in banned_users:
        user = ban_entry.user
        
        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Banned{member.mention}')
            return


@bot.command(pass_context=True)
async def magic8ball(ctx):
    await ctx.channel.send(random.choice(["It is certain :8ball: ",
                                          "Banana :8ball: ",
                                          "Dirolo cottage :8ball: ",
                                          "Paris is an asshole :8ball: ",
                                          "Wlu gaming :8ball: ",
                                          "Hello :8ball: %s!" % ctx.message.author.mention,
                                          "Viki katsikali :8ball: ",




    
    
    ]))

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Color.purple()
    )
    embed.set_author(name="Addiction Bot - Help and Documentation")
    embed.add_field(name="a!help", value="Your using it right now", inline=False)
    embed.add_field(name="a!avatar", value="You can see your avatar", inline=False)
    embed.add_field(name="a!profile", value="You can see your profile", inline=False)
    embed.add_field(name="a!magic8ball", value="Random things with magic 8 ball", inline=False)
    embed.add_field(name="a!kick", value="You can kick members", inline=False)
    embed.add_field(name="a!clear", value="You can clear message", inline=False)
    embed.add_field(name="a!info", value="You can take info about bot", inline=False)
    embed.add_field(name="a!datetime", value="You can see the datetime ", inline=False)
    embed.add_field(name="a!ban", value="You can ban ", inline=False)
    embed.add_field(name="a!unban", value="You can unban ", inline=False)
    embed.add_field(name="a!say", value="Say bot what you said ", inline=False)
    embed.add_field(name="a!reply", value="He answers you the addiction bot ", inline=False)
    

    await ctx.channel.send("I sent you a dm!")
    await author.send(embed=embed)






@bot.command()
async def datetime(ctx):
    await ctx.channel.send(f"This message was sent on: {ctx.message.created_at}")


    
    
@bot.command()
async def say(ctx, *, something):
    """Say something!"""
    if something is None:
        await ctx.send("What do you want to say?")
        return
        
    await ctx.send(f"{ctx.message.author.mention} said: **{something}**")

 


@bot.command()
async def reply(ctx,*,question):
    responses = ["yes", "maybe","no"]
    await ctx.send(f"question: {question}\nanswer: {random.choice(responses)} ")






bot.run("NTc5MzU1NjEwMjY5NzQ1MTgz.XWPNlA.FS7raFVqBcp_ie6HmX0-LRnSWbg")
