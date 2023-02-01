import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
import asyncio

with open("setting.json",mode = "r",encoding="utf8") as file:
    data = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

class Test(Cog_Extension):
    @commands.command()
    async def embed(ctx,self):
        embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
        await ctx.send(embed=embed)













async def setup(bot):
    await bot.add_cog(Test(bot))