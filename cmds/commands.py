from genericpath import commonprefix
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

from core.classes import Cog_extension 


class Cmds(Cog_extension):

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)")

    @commands.command()
    async def picture(self,ctx):
        pic = discord.File("C:\\Users\\User\\Downloads\\下載.jfif")
        await ctx.send(file=pic)
        
        

def setup(bot):
    bot.add_cog(Cmds(bot))