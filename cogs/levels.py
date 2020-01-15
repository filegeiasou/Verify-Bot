import discord
from discord.ext import commands

class Levels:
	def __init__(self,bot):
		self.bot = bot


def setupt(bot):
	bot.add_cog(Levels(bot))