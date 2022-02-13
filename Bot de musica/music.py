import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #Faça o bot entrar qnd o usuario entrar tb
    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None: #Se n tem ninguem
            await ctx.send("VC tem que entrar, seu burro.")
        chamada = ctx.autor.voice.channel
        if ctx.voice_client is None:
            await chamada.connect()
        else:
            await ctx.voice_client.move_to(chamada)

    @commands.command() #esse faz o inverso
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconect_delay_max 5', 'options': 'vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'] [0] ['url']
            source = await discord.FFmpegOpusAudio.form_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
    
    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pausar()
        await ctx.send("pausar")
    
    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("vai")

    


def setup(client):
    client.add_cog(music(client))