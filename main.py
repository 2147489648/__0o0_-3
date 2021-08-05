from webserver import keep_alive

import os

import discord
from discord.ext import commands
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True

bot = commands.Bot(command_prefix="[", intents=intents, owner_id=633082846138990614)

@bot.event
async def on_ready():
    print(">> __0o0_ 的專屬機械人在線了 <<")
    channel = bot.get_channel(795641935540912179)
    await channel.send('>> \_\_0o0\_ 的專屬機械人在線了 <<')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension}.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension}.')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension}.')

for Filename in os.listdir('./cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == "__main__":
  keep_alive()
  TOKEN = os.environ.get("DISCORD_BOT_SECRET")
  bot.run(TOKEN)