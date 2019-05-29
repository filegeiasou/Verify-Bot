import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="!", status=discord.Status.online, activity=discord.Game(name="Made by filegeiasou#0935"))


@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")
    await bot.change_presence(activity=discord.Game(name="Made by filegeiasou#0935"))

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="welcome")
    await member.send(f"Welcome {member.mention}😀")


@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="goodbye")
    await member.send(f"Goodbye {member.mention}:sob:")


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
        title="What Lies Underneath",
        description="What lies underneath server : https://discord.gg/cwerZuM. What lies underneath site : https://whatliesunderneath.cf/.",
        colour=discord.Colour.orange()
    )

    testembed.set_author(name="Verifynow")
    testembed.set_footer(text="Wlu team")

    await ctx.channel.send(embed=testembed)


@bot.command()
async def verify(ctx):
    testembed = discord.Embed(
        title="Verify bot",
        description="Verify bot and site here : http://verifynow.cf/.",
        colour=discord.Colour.blue()
    )

    testembed.set_author(name="Verifynow")
    testembed.set_footer(text="Wlu team")

    await ctx.channel.send(embed=testembed)


@bot.command()
async def site(ctx):
    testembed = discord.Embed(
        title="Verify bot",
        description="Everyone who wants to help with bot send email here : http://verifynow.cf/.",
        colour=discord.Colour.purple()
    )

    testembed.set_author(name="Verifynow")
    testembed.set_footer(text="Wlu team")

    await ctx.channel.send(embed=testembed)


bot.run("NTc5MzU1NjEwMjY5NzQ1MTgz.XO4fnw.2ogeadLZ7bsQqO9JL-Sc1MPhGJM")
