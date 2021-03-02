import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '[')

@bot.event
async def on_ready():
   print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
   channel = bot.get_channel(816327091146326056)
   await channel.send(f'{member} join!')

bot.run("ODE1Nzk2NzkxNjg1NDE0OTEy.YDxn9w.QLZ9PzZJtmLE5y4X3hG4tCn39Jk")