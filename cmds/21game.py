import discord
from discord.ext import commands
import random
import json
from core.classes import Cog_Extension

with open("setting.json",mode = "r",encoding="utf8") as file:
    data = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

class GameP(Cog_Extension):
    @commands.command()
    async def game1(self, ctx):
    
        # 檢查回傳的是否是同一個人(已及是否在同一個頻道)
        def check(number):
            return number.author == ctx.author and number.channel == ctx.message.channel
        BOT_END = 17 #莊家到多少停牌
        CARD = 1
        for i in range(1): 
            #>>>創建list<<<#
            number = []
            for j in range(CARD): #你要幾副牌
                for i in range(4):
                    for j in range(1,11):
                        number.append(j)
                    number.append(10)
                    number.append(10)
                    number.append(10)
            #>>>二次打亂<<<#
            numbers = []
            for i in range(len(number)):
                rand_num = random.choice(number)
                number.remove(rand_num)
                numbers.append(rand_num)
            #>>>製作遊戲<<<#

            #>>>計算次數<<<#
            people_n = 0
            bot_n = 0
            people_count = 2
            bot_count = 2
            giveacard = ""
            #>>>初始手牌<<<#
            rand_num = random.choice(numbers)
            numbers.remove(rand_num)
            people_n += rand_num
            rand_num = random.choice(numbers)
            numbers.remove(rand_num)
            bot_n += rand_num
            rand_num = random.choice(numbers)
            numbers.remove(rand_num)
            people_n += rand_num
            rand_num = random.choice(numbers)
            numbers.remove(rand_num)
            bot_n += rand_num
            embed = discord.Embed(title="21點遊戲",description="目前遊戲",color=0xeee657)
            embed.add_field(name="目前進度",value="莊家第一張牌為:%d\n目前玩家手牌:%d\n目前手牌有%d張"%(rand_num,people_n,people_count),inline=False)
            embed.add_field(name="請輸入",value="抽牌/停牌  y/n",inline=False)
            await ctx.send(embed=embed)
            #>>>遊戲開始<<<#
            while True:
                #>>>輸入<<<#
                response = await self.bot.wait_for('message', check = check)            
                try : 
                    giveacard = response.content 
                except:
                    embed = discord.Embed(title="21點遊戲",description="目前遊戲",color=0xeee657)
                    embed.add_field(name="請輸入",value="抽牌/停牌  y/n",inline=False)
                    await ctx.send(embed=embed)
                if giveacard == "停止":
                    embed = discord.Embed(title="21點遊戲",description="遊戲停止",color=0xeee657)
                    embed.add_field(name="內容",value="終止所有遊戲",inline=False)
                    await ctx.send(embed=embed)
                    break
                if giveacard=="y":
                    rand_num = random.choice(numbers)
                    numbers.remove(rand_num)
                    people_n += rand_num
                    people_count+=1
                    embed = discord.Embed(title="21點遊戲",description="目前遊戲",color=0xeee657)
                    embed.add_field(name="目前進度",value="玩家抽牌:%d\n目前玩家手牌:%d\n目前手牌有%d張\n目前莊家手牌有%d張"%(rand_num,people_n,people_count,bot_count),inline=False)
                    await ctx.send(embed=embed)
                    giveacard = ""
                if bot_n <= BOT_END and people_n <=21:
                    rand_num = random.choice(numbers)
                    numbers.remove(rand_num)
                    bot_n += rand_num
                    bot_count+=1
                    embed = discord.Embed(title="21點遊戲",description="目前遊戲",color=0xeee657)
                    embed.add_field(name="目前進度",value="莊家抽牌:XX\n目前莊家手牌有%d張\n目前玩家手牌:%d\n目前玩家手牌有%d張"%(bot_count,people_n,people_count),inline=False)
                    await ctx.send(embed=embed)
                
                if people_n > 21 or bot_count >= 5:
                    embed = discord.Embed(title="21點遊戲",description="遊戲資料",color=0xeee657)
                    embed.add_field(name="勝負",value="玩家輸了",inline=False)
                    embed.add_field(name="總得點數",value="玩家得點:%d\t莊家得點:%d"%(people_n,bot_n),inline=False)
                    await ctx.send(embed=embed)
                    break
                if bot_n > 21 or people_count >= 5:
                    embed = discord.Embed(title="21點遊戲",description="遊戲資料",color=0xeee657)
                    embed.add_field(name="勝負",value="莊家輸了",inline=False)
                    embed.add_field(name="總得點數",value="玩家得點:%d\t莊家得點:%d"%(people_n,bot_n),inline=False)
                    await ctx.send(embed=embed)
                    break
                if giveacard == "n" and bot_n >= BOT_END:
                    if people_n > bot_n:
                        embed = discord.Embed(title="21點遊戲",description="遊戲資料",color=0xeee657)
                        embed.add_field(name="勝負",value="莊家輸了",inline=False)
                        embed.add_field(name="總得點數",value="玩家得點:%d\t莊家得點:%d"%(people_n,bot_n),inline=False)
                        await ctx.send(embed=embed)
                        break
                    elif people_n < bot_n:
                        embed = discord.Embed(title="21點遊戲",description="遊戲資料",color=0xeee657)
                        embed.add_field(name="勝負",value="玩家輸了",inline=False)
                        embed.add_field(name="總得點數",value="玩家得點:%d\t莊家得點:%d"%(people_n,bot_n),inline=False)
                        await ctx.send(embed=embed)
                        break
                    else:
                        embed = discord.Embed(title="21點遊戲",description="遊戲資料",color=0xeee657)
                        embed.add_field(name="勝負",value="平手",inline=False)
                        embed.add_field(name="總得點數",value="玩家得點:%d\t莊家得點:%d"%(people_n,bot_n),inline=False)
                        await ctx.send(embed=embed)
                        break
        
        

               
async def setup(bot):
    await bot.add_cog(GameP(bot))