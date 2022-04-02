from genericpath import commonprefix
import discord
from discord.ext import commands
import json

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
    await channel.sned(f"{member} hello!")
    print(f"{member}join!")

@bot.event
async def on_member_remove(member):
    print(f"{member}leave!")

@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)}(ms)")
    
bot.run(setting["TOKEN"])

