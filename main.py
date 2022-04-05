from genericpath import commonprefix
import isort

import discord
from discord.ext import commands
import json
import os



intents = discord.Intents.all()

with open("setting.json", mode="r",encoding="utf8") as s_json:
    setting = json.load(s_json)

bot = commands.Bot(command_prefix="!", intents = intents)

 
@bot.event
async def on_ready():
    print("bot is online")
    


for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(setting["TOKEN"])

