import discord
from discord.ext import commands
import json
import os
import asyncio


with open("setting.json",mode = "r",encoding="utf8") as file:
    data = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print('>>>bot is online<<<')
    game = discord.Game('尋找乾爹斗內')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)


@bot.command()
async def load(ctx,extension):
    uid = ctx.author.id
    if uid == 345491739664187393:
        await bot.load_extension(f'cmds.{extension}')
        await ctx.send(f"安裝 {extension} 好了")
    else:
        tmpmsg = await ctx.send(f'<@{uid}> 你沒有此權限 !')
        await asyncio.sleep(3)
        await tmpmsg.delete()


@bot.command()
async def unload(ctx,extension):
    uid = ctx.author.id
    if uid == 345491739664187393:
        await bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f"卸載 {extension} 好了")
    else:
        tmpmsg = await ctx.send(f'<@{uid}> 你沒有此權限 !')
        await asyncio.sleep(3)
        await tmpmsg.delete()

@bot.command()
async def reload(ctx,extension):
    uid = ctx.author.id
    if uid == 345491739664187393:
        await bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f"重載 {extension} 好了")
    else:
        tmpmsg = await ctx.send(f'<@{uid}> 你沒有此權限 !')
        await asyncio.sleep(3)
        await tmpmsg.delete()

async def load():
    for filename in os.listdir("./cmds"):
        print(filename)
        if filename.endswith(".py"):
            await bot.load_extension(f'cmds.{filename[:-3]}')

async def BOT():
    await load()
    await bot.start(data["TOKEN"])

    
asyncio.run(BOT())