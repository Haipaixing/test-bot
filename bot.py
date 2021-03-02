import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
   print(">> Bot is online <<")

bot.run("ODE1Nzk2NzkxNjg1NDE0OTEy.YDxn9w.nedwjAuPLow8ni08XNU-p2OZCGk")