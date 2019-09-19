import discord
import asyncio
import random
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from itertools import cycle

status = cycle([ "Made by filegeiasou", "write !help" ])
bot = commands.Bot(command_prefix="!", status=discord.Status.online, activity=discord.Game(name="Made by filegeiasou#0935"))

bot.remove_command('help')
@bot.event
async def on_ready():
    change_status.start()
    print(f"{bot.user.name} is ready")
    await bot.change_presence(activity=discord.Game(name="Made by filegeiasou#0935"))

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await member.send(f"Welcome {member.mention}😀")
    role = discord.utils.get(member.guild.roles, name="Oberdeckoffizier")
    await member.add_roles(role)

@tasks.loop(seconds=8)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))




@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="goodbye")
    await member.send(f"Goodbye {member.mention}:sob:")

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
async def ping(ctx):
    await ctx.channel.send("Pong, %s!" % ctx.message.author.mention)


@bot.command()
async def info(ctx):
    await ctx.author.send("Do you like to help me with command send me email here: filegeiasou@gmail.com.")



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


@bot.command(pass_context=True)
async def hi(ctx):
    await ctx.channel.send("Hello, %s!" % ctx.message.author.mention)


@bot.command(pass_context=True)
async def magic8ball(ctx):
    await ctx.channel.send(random.choice(["It is certain :8ball: ",
                                          "Banana :8ball: ",
                                          "Dirolo cottage :8ball: ",
                                          "Paris is an asshole :8ball: ",
                                          "Wlu gaming :8ball: ",
                                          "Hello :8ball: %s!" % ctx.message.author.mention,




    
    
    ]))

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Color.purple()
    )
    embed.set_author(name="Verify Bot - Help and Documentation")
    embed.add_field(name="!help", value="Your using it right now", inline=False)
    embed.add_field(name="!avatar", value="You can see your avatar", inline=False)
    embed.add_field(name="!alexsss", value="Who is Alexsss", inline=False)
    embed.add_field(name="!wlu", value="Wlu game ", inline=False)
    embed.add_field(name="!site", value="The website of bot", inline=False)
    embed.add_field(name="!profile", value="You can see your profile", inline=False)
    embed.add_field(name="!magic8ball", value="Random things with magic 8 ball", inline=False)
    embed.add_field(name="!hi", value="Hello", inline=False)
    embed.add_field(name="!kick", value="You can kick members", inline=False)
    embed.add_field(name="!clear", value="You can clear message", inline=False)
    embed.add_field(name="!info", value="You can take info about bot", inline=False)
    embed.add_field(name="!ping", value="Pong", inline=False)
    embed.add_field(name="!datetime", value="You can see the datetime ", inline=False)
    embed.add_field(name="!verify", value="You can verify your account", inline=False)

    await ctx.channel.send("I sent you a dm!")
    await author.send(embed=embed)






@bot.command()
async def datetime(ctx):
    await ctx.channel.send(f"This message was sent on: {ctx.message.created_at}")


@bot.command()
async def wlu(ctx):
    testembed = discord.Embed(
        title="What Lies Underneath",
        description="What lies underneath server : https://discord.gg/cwerZuM. What lies underneath site : https://whatliesunderneath.cf/.",
        colour=discord.Colour.orange()
    )

    testembed.set_author(name="Verifynow")
    testembed.set_footer(text="Wlu team")

    await ctx.channel.send(embed=testembed)

@bot.command()
async def alexsss(ctx):
    alexsssembed = discord.Embed(
        title = "AlexSSS",
        description = "AlexSSS makes Devo, a featureful Discord bot. Add it at https://devo.xyz/ ! He also makes i.devo, a fluent file host that just works. Check it out at http://i.devo.xyz/. Lastly, he sometimes streams. Watch them at https:/bit.ly/alexsss/ !",
        colour = discord.Colour.green()
    )

    await ctx.channel.send(embed=alexsssembed)

@bot.command()
async def verify(ctx):
    testembed = discord.Embed(
        title="Verify bot",
        description="Verify bot and site here : http://verifynow.cf/.",
        colour=discord.Colour.blue()
    )

    testembed.set_author(name="Verifynow")
    testembed.set_footer(text="Verify team")

    await ctx.channel.send(embed=testembed)


@bot.command()
async def site(ctx):
    testembed = discord.Embed(
        title="Verify bot",
        description="Everyone who wants to help with bot send email here : http://verifynow.cf/.",
        colour=discord.Colour.purple()
    )

    testembed.set_author(name="Verifynow")
    testembed.set_footer(text="Verify team")

    await ctx.channel.send(embed=testembed)


bot.run("NTc5MzU1NjEwMjY5NzQ1MTgz.XWPNlA.FS7raFVqBcp_ie6HmX0-LRnSWbg")
