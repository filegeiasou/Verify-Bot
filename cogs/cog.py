import discord 

from discord.ext import commands

class TestCog:
    counter = 0

    def __init__(self, bot):
        self.bot = bot
        self.bot.command()(self.add)

    async def add(self):
        TestCog.counter += 1
        await self.bot.say('Counter is now %d' % TestCog.counter)
def setup(bot):
    bot.add_cog(TestCog(bot))