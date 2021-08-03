import discord
from discord.ext import commands
from core.classes import Cog_Extension
import global_
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Bank(Cog_Extension):
    @commands.command()
    async def revise(self, ctx):
        await ctx.send(jdata['REVISE'])
 
    @commands.command()
    async def bank(self, ctx, msg, value:int):
      if ctx.author.id == 633082846138990614:
        if msg == 'add':
          global_.score += value
          await ctx.channel.purge(limit=1)
          await ctx.send('You have ${} now!'.format(global_.score))
        elif msg == 'remove':
          global_.score -= value
          await ctx.channel.purge(limit=1)
          await ctx.send('You have ${} now!'.format(global_.score))
        elif msg == 'show':
          await ctx.send('You have ${} now!'.format(global_.score))
      else:
          await ctx.send("\_\_0o0\_ has ${} now!".format(global_.score))
    @commands.command()
    async def inventory(self, ctx, msg):
      if msg == 'show':
        embed=discord.Embed(title="Inventory", description="Here is \_\_0o0\_'s inventory", color=0x8f4500)
        embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
        x = 0
        if len(global_.inventory) > 0:
          while len(global_.inventory) > x:
            embed.add_field(name="Name", value=global_.inventory[x], inline=True)
            b = 0
            while len(global_.items[0]) > b:
              if global_.items[0][b] == global_.inventory[x]:
                embed.add_field(name="Description", value=global_.items[1][b], inline=True)
                embed.add_field(name="Rarity", value=global_.items[3][b], inline=True)
                embed.set_footer(text="Created by __0o0_#5740")
                b += 1                
              else:
                b += 1
            x += 1
          await ctx.send(embed=embed)
        else:
          embed=discord.Embed(color=0xff0000)
          embed.add_field(name="Error", value="You do not have any items in your inventory", inline=False)
          await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Bank(bot))