import discord
from discord.ext import commands
import json
from core.classes import Cog_Extension
import asyncio
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

with open("setting.json",mode = "r",encoding="utf8") as file:
    data = json.load(file)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='', intents=intents)

class Ig(Cog_Extension):

    @commands.command()
    async def search(self,ctx, *, query):
        await ctx.send("aawawa")
        PATH = Service("C:/Users/User/Desktop/chromedriver.exe")
        driver = webdriver.Chrome(service=PATH)
        driver.get("https://www.instagram.com/accounts/login/")
        wait = WebDriverWait(driver, 10)

        username = "chenisa87"
        wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password = "aa02765258"
        wait.until(EC.presence_of_element_located((By.NAME, "password")))

        username.send_keys("YOUR_USERNAME")
        password.send_keys("YOUR_PASSWORD")
        password.send_keys(Keys.RETURN)

        search_bar = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="搜尋"]')))
        search_bar.send_keys(query)
        search_bar.send_keys(Keys.RETURN)
        image_xpath = '//img[@class="FFVAD"]'
        image = wait.until(EC.presence_of_element_located((By.XPATH, image_xpath)))
        image_url = image.get_attribute("src")
        await ctx.send(image_url)
        # 關閉瀏覽器
        driver.quit()

async def setup(bot):
    await bot.add_cog(Ig(bot))  