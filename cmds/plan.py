import discord
from discord.ext import commands
from core.classes import Cog_Extension
import global_
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Plan(Cog_Extension):
    @commands.command()
    async def revise(self, ctx):
        await ctx.send(jdata['REVISE'])
 
    @commands.command()
    async def bank(self, ctx, msg, value:int):
      if msg == 'change':
        if ctx.author.id == 633082846138990614:
          global_.score += value
          await ctx.channel.purge(limit=1)
          await ctx.send('You have ${} now!'.format(global_.score))
        else:
          await ctx.send("__0o0_ has ${} now!".format(global_.score))
      elif msg == 'show':
        if ctx.author.id == 633082846138990614:
          await ctx.send('You have ${} now!'.format(global_.score))
        else:
          await ctx.send("__0o0_ has ${} now!".format(global_.score))




def setup(bot):
    bot.add_cog(Plan(bot))