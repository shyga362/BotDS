import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.intent.all())

for 1 in range(len(cogs)):
    cogs[1].setup()


client.Run('OTA0Nzg2MDE2ODQ4NzE1ODE2.YYAlpA.D7gIb8AuD2MEpY79htvMIS4Ws90')