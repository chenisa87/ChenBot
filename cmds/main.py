import discord
from discord.ext import commands
from core.classes import Cog_Extension

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

class Main(Cog_Extension):
    
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(F'{round(self.bot.latency*1000)}(ms)')


    #>>>功能表<<<#

    @commands.command()
    async def 功能表(self,ctx):
        embed = discord.Embed(title="功能表", description="內容", color=0xeee657)
        embed.add_field(name="管理員指令", value="$unload $load $reload", inline=False)
        embed.add_field(name="基礎指令", value="$help $功能表 $文靜功能表", inline=False)
        embed.add_field(name="嘎逼指令", value="嘎逼 早安/午安/晚安 | 汪", inline=False)    
        await ctx.send(embed=embed)

    @commands.command()
    async def 文靜功能表(self,ctx):
        embed = discord.Embed(title="文靜功能表", description="內容", color=0xeee657)
        embed.add_field(name="強化試算表", value="$強化", inline=False)    
        await ctx.send(embed=embed)




async def setup(bot):
    await bot.add_cog(Main(bot))  




