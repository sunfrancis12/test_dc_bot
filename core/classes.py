from genericpath import commonprefix

from isort import file
import discord
from discord.ext import commands
import json

class Cog_extension(commands.Cog):
    def  __init__(self,bot):
        self.bot = bot
