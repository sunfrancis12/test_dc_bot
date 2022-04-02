from genericpath import commonprefix

from isort import file
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
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(701804743206502453) 
    await channel.send(f"{member} hello!")
    print(f"{member}join!")

@bot.event
async def on_member_remove(member):
    print(f"{member}leave!")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(setting["TOKEN"])

