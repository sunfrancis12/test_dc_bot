from genericpath import commonprefix
import discord
from discord.ext import commands

from core.classes import Cog_extension

intents = discord.Intents.all()


class Event(Cog_extension):

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(701804743206502453) 
        await channel.send(f"{member} hello!")
        print(f"{member}join!")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f"{member}leave!")
    
    

def setup(bot):
    bot.add_cog(Event(bot))