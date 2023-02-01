import discord
from discord.ext import commands
from random import randint
import json
from core.classes import Cog_Extension

with open("setting.json",mode = "r",encoding="utf8") as file:
    data = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

class GameT(Cog_Extension):
    @commands.command()
    async def game2(self, ctx):
    
        # 檢查回傳的是否是同一個人(已及是否在同一個頻道)
        def check(number):
            return number.author == ctx.author and number.channel == ctx.message.channel

        async def map(list):
            map_list = list
            embed = discord.Embed(title="圈圈叉叉遊戲",description="遊戲板子",color=0xeee657)
            embed.add_field(name="------------",value="-%s--%s--%s-"%(map_list[0],map_list[1],map_list[2]),inline=False)
            embed.add_field(name="------------",value="-%s--%s--%s-"%(map_list[3],map_list[4],map_list[5]),inline=False)
            embed.add_field(name="------------",value="-%s--%s--%s-"%(map_list[6],map_list[7],map_list[8]),inline=False)
            embed.add_field(name="------------",value="這只是板子",inline=False)
            await ctx.send(embed=embed)

        async def map_p(list,n):
            map_p_l = list
            if map_p_l[n-1] == "#":
                map_p_l[n-1] = "O"
            else:
                await ctx.send("請再輸入一次:")
                response = await self.bot.wait_for('message', check = check)            
                try: 
                    n = response.content
                except:
                    map(map_l)
                map_p(map_p_l,n)

            return map_p_l
        
            


        async def map_b(list):
            map_b_l = list
            n = randint(1,9)
            if map_b_l[n-1] == "#":
                map_b_l[n-1] = "X"
            else:
                await map_b(map_b_l)
            return map_b_l

        async def checkwin(list):
            map_w = list
            for i in range(3):
                check_p = 0
                check_b = 0
                for j in range(i*3,3*(i+1)):
                    check_p += 1 if map_w[j] == "O" else 0 
                    check_b += 1 if map_w[j] == "X" else 0
                if check_b == 3:
                    return "bot_win"
                elif check_p == 3:
                    return "people_win"
                check_p = 0
                check_b = 0
                for j in range(i,9,3):
                    check_p += 1 if map_w[j] == "O" else 0 
                    check_b += 1 if map_w[j] == "X" else 0
                if check_b == 3:
                    return "bot_win"
                elif check_p == 3:
                    return "people_win"
            if map_w[0] == "O" and map_w[4] == "O" and map_w[8] == "O":
                return "people_win"
            elif map_w[0] == "X" and map_w[4] == "X" and map_w[8] == "X":
                return "bot_win"
            elif map_w[2] == "O" and map_w[4] == "O" and map_w[6] == "O":
                return "people_win"
            elif map_w[2] == "X" and map_w[4] == "X" and map_w[6] == "X":
                return "bot_win"
            else:
                return "nothing"



        
        map_l = ["#","#","#","#","#","#","#","#","#"]  
        await map(map_l) 
        while True:
            await ctx.send("請問你要在哪一格:")
            response = await self.bot.wait_for('message', check = check)            
            try: 
                n = int(response.content)
            except:
                map(map_l)
            map_l = await map_p(map_l,n)
            await map(map_l)
            if await checkwin(map_l) == "people_win":
                await ctx.send("恭喜你獲勝!")
                break
            elif await checkwin(map_l) == "bot_win":
                await ctx.send("對方獲勝 T_T ")
                break
            else:
                pass
            map_l = await map_b(map_l)
            await map(map_l)
            if await checkwin(map_l) == "people_win":
                await ctx.send("恭喜你獲勝!")
                break
            elif await checkwin(map_l) == "bot_win":
                await ctx.send("對方獲勝 T_T ")
                break
            else:
                pass


        
        

               
async def setup(bot):
    await bot.add_cog(GameT(bot))