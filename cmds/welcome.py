from genericpath import commonprefix


import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import youtube_dl
import asyncio
import os

from core.classes import Cog_extension


class Welcome(Cog_extension):
    
    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before, after):
        if not before.channel and after.channel:
            channel = member.voice.channel
            text = self.bot.get_channel(701804743206502453)
            await text.send(f'{member} joined')

            await channel.connect()

            vc = channel.guild.voice_client

            YDL_OPTIONS = {'format':"bestaudio"}
            FFMPEG_OPTIONS = {'before_options':"-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",'options':"-vn"}

            
            f = open(f"C:\\Users\\sunfrancis12\\OneDrive\\文件\\GitHub\\test_dc_bot\\cmds\\list\\{member}.txt","r")
            url = f.read()
            f.close()


            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info =ydl.extract_info(url,download=False)
                url2 = info["formats"][0]["url"]
                source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
                vc.play(source)

            #source = FFmpegPCMAudio("C:\\Users\\User\\Downloads\\Discord Ringing sound (For Trolling).mp3")
            #vc = channel.guild.voice_client
            #vc.play(source)
            while vc.is_playing():
                await asyncio.sleep(1)
            vc.stop()
            await vc.disconnect()
    
    @commands.command()
    async def bgm(self,ctx,arg):
        
        f = open(f"{ctx.author}.txt","w+")
        f.write(arg)
        f.close()

        src=f'C:\\Users\\sunfrancis12\\OneDrive\\文件\\GitHub\\test_dc_bot\\{ctx.author}.txt'
        des=f'C:\\Users\\sunfrancis12\\OneDrive\\文件\\GitHub\\test_dc_bot\\cmds\\list\\{ctx.author}.txt'
        

        os.replace(src,des)

        ctx.send(f"使用者 = {ctx.author}, 網址= {arg}")
        
        print(ctx.author)
        print(arg)

def setup(bot):
    bot.add_cog(Welcome(bot))