import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
import asyncio

with open("setting.json",mode = "r",encoding="utf8") as file:
    data = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

class 模板(Cog_Extension):
    """
    內容
    """


async def setup(bot):
    await bot.add_cog(模板(bot))  