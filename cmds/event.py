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

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self,msg):
        if "嘎逼" in msg.content and msg.author != self.bot.user:
            if "愛你" in msg.content:
                await msg.channel.send("汪!我也愛你")
            elif "晚安" in msg.content:
                await msg.channel.send("汪!晚安")      
            elif "午安" in msg.content:
                await msg.channel.send("汪!午安")             
            elif "早安" in msg.content:
                await msg.channel.send("汪!早安")
            else:
                await msg.channel.send("汪!怎麼了嗎 愛你/晚安/早安")
        
        #陳信宇閉嘴
        #if msg.author.id == 963716136959082528:
        #    tmpmsg =  await msg.channel.send("<@963716136959082528> 閉嘴啦!")
        #    await tmpmsg.delete()
        if "分數" in msg.content and msg.author != self.bot.user:
            await msg.channel.send("請輸入:$計算成績 國文 英文 數學 物理 化學 生物 地科 地理 歷史 公民")   
        #排除自己的訊息，避免陷入無限循環
        if msg.author == self.bot.user:
            return
        #如果以「說」開頭
        if "汪" in msg.content and msg.author != self.bot.user:
            tmp = msg.content.split(" ")
            if tmp[0] == "汪":
            #如果分割後串列長度只有1
                if len(tmp) ==1:
                    await msg.channel.send("哩喜哩汪三小")
                else:
                    del tmp[0]
                    tmp_str = " ".join(tmp)
                    await msg.channel.send(tmp_str)
        if msg.content.startswith('更改狀態'):
            #切兩刀訊息
            tmp = msg.content.split(" ",2)
            #如果分割後串列長度只有1
            if len(tmp) == 1:
                await msg.channel.send("你要改成什麼啦？")
            else:
                game = discord.Game(tmp[1])
                #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
                await self.bot.change_presence(status=discord.Status.idle, activity=game) 
    

async def setup(bot):
    await bot.add_cog(Event(bot))