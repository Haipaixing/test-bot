import discord

from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
   print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    print(f"{member.mention} join")

bot.run("ODE1Nzk2NzkxNjg1NDE0OTEy.YDxn9w.CxG9bKjBASzaMmaq6383et_aXvM")