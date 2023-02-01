import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
import asyncio

with open("setting.json",mode = "r",encoding="utf8") as file:
    data = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

class Trade(Cog_Extension):
    @commands.command()
    async def 交易(self,ctx):
        uid = ctx.author.id
        if uid == 345491739664187393:
            await ctx.send("<@345491739664187393>")
            embed = discord.Embed(title="丞丞的商品", description="公會一丞丞的商店(向日葵)", color=0xeee657)

            #>>>裝備<<<#
            embed.add_field(name=">>>>>裝備<<<<<", value="其他也可以來問", inline=False)
            embed.add_field(name="帽子", value="夏日10組6天", inline=False)
            embed.add_field(name="胸甲", value="混蓋16詛 聖龍甲2歐8聖", inline=False)
            embed.add_field(name="褲子", value="公主10組", inline=False)
            embed.add_field(name="鞋子", value="火山5歐9惡2天全過", inline=False)
            embed.add_field(name="寵物", value="公主10組(售出)", inline=False)
            embed.add_field(name="副手", value="混蓋16組", inline=False)
            embed.add_field(name="腰帶", value="夏日14 +25 夏日14 +14", inline=False)
            embed.add_field(name="披風", value="眾靈16", inline=False)
            embed.add_field(name="綴飾", value="火山5歐9惡", inline=False)
            embed.add_field(name="勳章", value="八周12組(無視防禦)", inline=False)
            embed.add_field(name="披肩", value="夏日16組", inline=False)
            embed.add_field(name="戒指", value="極光14組", inline=False)

            #>>>奧義<<<#

            embed.add_field(name=">>>>>奧義<<<<<", value="全都+10 大多4傳10完美", inline=False)
            embed.add_field(name="天啟", value="致命地雷 蒼翠魔晶之心 祝福炎脈(售出) 黎明的地平線", inline=False)
            embed.add_field(name="命格", value="焰日意念 吞噬者 空間立方體 自由使命 ", inline=False)
            embed.add_field(name="烈陽", value="炎赫暉陽 萬物法則 琉螢盛夏幻曲 學院烈陽 薩拉曼德之魂", inline=False)

            #>>>加工產品<<<#

            embed.add_field(name=">>>>>加工產品<<<<<", value="都可以問", inline=False)
            embed.add_field(name="飾品", value="炎//森之飾品 炎//森變換石", inline=False)
            embed.add_field(name="裝備", value="公主10詛咒 祝福套", inline=False)

            #>>>雜物<<<#

            embed.add_field(name=">>>>>雜物<<<<<", value="有就賣", inline=False)
            embed.add_field(name="技能卷軸", value="私我問", inline=False)
            
        else:
            tmpmsg = await ctx.send(f'<@{uid}> 你沒有此權限 !')
            await asyncio.sleep(3)
            await tmpmsg.delete()


        await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Trade(bot))