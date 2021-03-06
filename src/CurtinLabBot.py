import discord
from discord.ext import commands, tasks
import aiohttp
import asyncio
from config import getToken
from Labs import Labs
from Webserver import Webserver
from BrayPull import BrayPull
from SheetPull import SheetPull
from Lab import Lab

bot = commands.Bot(command_prefix="^", case_insensitive=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Loading..."))

if __name__ == "__main__":
    bot.add_cog(Labs(bot))
    bot.add_cog(Webserver(bot))
    #bot.add_cog(BrayPull(bot))
    bot.add_cog(SheetPull(bot))
    print("Bot starting")
    bot.run(getToken("./persistence/config.ini"))