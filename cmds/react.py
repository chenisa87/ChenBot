import discord
from discord.ext import commands
import random
import json
from core.classes import Cog_Extension
import calendar
import asyncio
#import datetime

with open("setting.json",mode = "r",encoding="utf8") as file:
    data = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

class React(Cog_Extension):

    @commands.command()
    async def 早安(self,ctx):
        random_choice = random.choice(data["goodmorning"])
        pic = discord.File(random_choice)
        await ctx.send(file = pic)

    @commands.command()
    async def 午安(self,ctx):
        random_choice = random.choice(data["123"])
        pic = discord.File(random_choice)
        await ctx.send(file = pic)

    @commands.command()
    async def 狗(self,ctx):
        await ctx.send("<@963716136959082528>  閉嘴拉")
    @commands.command()
    async def 上香(self,ctx):
        await ctx.send("(\\\_/)\n( •\_•)\n/ >\\\|/上香")
    @commands.command()
    async def 獻果(self,ctx):
        await ctx.send("(\\\_/)\n( •\_•)\n/ >:apple:獻果")
    @commands.command()
    async def 獻花(self,ctx):
        await ctx.send("(\\\_/)\n( •\_•)\n/ >:bouquet:獻花")
        

    @commands.command()
    async def 羽毛(self,ctx):
        await ctx.send("<@433994755068788738>  閉嘴拉")

    @commands.command()
    async def 蛋糕(self,ctx):
        await ctx.send("yyds")

    @commands.command()
    async def 可憐(self,ctx):
        pic = discord.File(data["pic1"])
        await ctx.send(file = pic)    
    @commands.command()
                    #  國文 英文 數學 物理 化學 生物 地科 地理 歷史 公民
    async def 計算成績(self,ctx,c:int,e:int,m:int,u:int,i:int,o:int,p:int,j:int,k:int,l:int):
        await ctx.send("總分加權後為%d"%(c*4+e*4+m*4+(u+i+o+p+j+k+l)*2))    

    @commands.command()
    async def 時間(self,ctx,year:int,month:int):
        embed = discord.Embed(title="時間 | 月份", color=0xeee657)
        embed.add_field(name="查詢結果", value=f'```{calendar.month(year,month)}```', inline=False)
        await ctx.send(embed=embed)
    #>>>強化<<<#

    @commands.command()
    async def 強化(self,ctx):
        embed = discord.Embed(title="強化表", description="請輸入:", color=0xeee657)
        embed.add_field(name="歐德惡魔", value="$強化1 素質 歐德 惡魔過 惡魔沒過 天使過 天使沒過 組防 強化次數", inline=False)
        embed.add_field(name="詛咒天使", value="$強化2 素質 詛咒 惡魔過 惡魔沒過 天使過 天使沒過 組防 強化次數", inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def 強化1(self,ctx,z:int,a:int,b:int,c:int,d:int,e:int,f:int,g:int):
        embed = discord.Embed(title="歐德惡魔", description="", color=0xeee657)
        embed.add_field(name="強化後素質", value="底標:%.2f    平均:%.2f    頂標:%.2f"%((z*(1.064**a)*(1.068**b)*(1**c)*(1.06**d)*(1.03**e)*(1.032**f)*(1.016**(g-f-e-d-c-b-a))),(z*(1.064**a)*(1.068**b)*(1**c)*(1.06**d)*(1.03**e)*(1.032**f)*(1.028**(g-f-e-d-c-b-a))),(z*(1.064**a)*(1.068**b)*(1**c)*(1.06**d)*(1.03**e)*(1.032**f)*(1.04**(g-f-e-d-c-b-a)))) , inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def 強化2(self,ctx,z:int,a:int,b:int,c:int,d:int,e:int,f:int,g:int):
        embed = discord.Embed(title="詛咒天使", description="", color=0xeee657)
        embed.add_field(name="強化後素質", value="底標:%.2f    平均:%.2f    頂標:%.2f"%((z*(1.08**a)*(1.068**b)*(1**c)*(1.06**d)*(1.03**e)*(1.032**f)*(1.016**(g-f-e-d-c-b-a))),(z*(1.08**a)*(1.068**b)*(1**c)*(1.06**d)*(1.03**e)*(1.032**f)*(1.028**(g-f-e-d-c-b-a))),(z*(1.08**a)*(1.068**b)*(1**c)*(1.06**d)*(1.03**e)*(1.032**f)*(1.04**(g-f-e-d-c-b-a)))) , inline=False)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(React(bot))  