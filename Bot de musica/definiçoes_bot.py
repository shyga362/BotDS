import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.intent.all())

for 1 in range(len(cogs)):
    cogs[1].setup()


client.Run('OTQyNDQyNzI5NDI4ODg5NjYw.YgkkMA.PugPDSpkCtl-5xob2d8GrzwV_Do')