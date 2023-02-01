import discord
from discord.ext import commands
import random
import json
import asyncio
from core.classes import Cog_Extension

with open("setting.json",mode = "r",encoding="utf8") as file:
    data = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

class Game(Cog_Extension):
    # cogs/guess.py
    @commands.command()
    async def guess(self, ctx):
    
        # 檢查回傳的是否是同一個人(已及是否在同一個頻道)
        def check(number):
            return number.author == ctx.author and number.channel == ctx.message.channel
        global lowernumber
        global highernumber
        
        lowernumber = 1
        highernumber = 100
        
        number = random.randint(lowernumber, highernumber)
        # print(number)
        
        await ctx.send('1-100任意選一個數字')
        
        for i in range(0, 5):    
            response = await self.bot.wait_for('message', check = check)
            
            try : 
                guess = int(response.content) 
            
            except:
                await ctx.send("請輸入數字")
                
            if guess == number : 
                await ctx.send("猜對了")
                break
                
            if guess > 100 :
                await ctx.send("超過100，格式錯誤")
                
            if guess < number:
                lowernumber = guess
                await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")
                
            if guess > number :
                highernumber = guess
                await ctx.send(f"比 {lowernumber}大，比 {highernumber} 小")
               
async def setup(bot):
    await bot.add_cog(Game(bot))