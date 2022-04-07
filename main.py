from genericpath import commonprefix

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

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f"cmd.{extension}")
    await ctx.send(f'loaded {extension}')
    
@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f"cmd.{extension}")
    await ctx.send(f'unloaded {extension}')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f"cmd.{extension}")
    await ctx.send(f'reloaded {extension}')

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    bot.run(setting["TOKEN"])

