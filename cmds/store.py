import discord
import json
from discord.ext import commands
from core.classes import Cog_Extension
import global_

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Store(Cog_Extension):
  @commands.command()
  async def store(self, ctx):
    embed=discord.Embed(title="Store", description="You can buy what you want in this store. Here are the items:", color=0xffd500)
    embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
    embed.set_thumbnail(url="https://i0.wp.com/www.animemaru.com/wp-content/uploads/2019/08/famima.jpg?w=640&ssl=1")
    a = 0
    while a < len(global_.items[0]):
      embed.add_field(name="Name", value=global_.items[0][a], inline=True)
      embed.add_field(name="Description", value=global_.items[1][a], inline=True)
      embed.add_field(name="Rarity", value=global_.items[3][a], inline=True)
      embed.add_field(name="Price", value="${}".format(global_.items[4][a]), inline=False)
      a += 1
    embed.set_footer(text="Created by __0o0_#5740")
    await ctx.send(embed=embed)
  @commands.command()
  async def buy(self, ctx, msg):
    b = 0
    while b < len(global_.items[0]):
      if msg == global_.items[0][b]:
        if global_.score >= global_.items[4][b]:
          embed=discord.Embed(title="Store", description="You have just successfully bought an item.", color=0x00ff62)
          embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
          embed.add_field(name="Name", value=global_.items[0][b], inline=True)
          embed.add_field(name="Description", value=global_.items[1][b], inline=True)
          embed.add_field(name="Rarity", value=global_.items[3][b], inline=True)
          embed.add_field(name="Price", value="${}".format(global_.items[4][b]), inline=False)
          embed.set_footer(text="Created by __0o0_#5740")
          await ctx.send(embed=embed)
          global_.score -= global_.items[4][b]
          await ctx.send('You have ${} now!'.format(global_.score))
          global_.inventory.append(global_.items[0][b])
          break
        else:
          embed=discord.Embed(color=0xff0000)
          embed.add_field(name="Not enough money", value="Sorry! You currently do not have enough money to buy {}. You need ${} more to buy this item".format(global_.items[0][b], global_.items[4][b]-global_.score), inline=False)
          embed.set_footer(text="Created by __0o0_#5740")
          await ctx.send(embed=embed)
          break
      b += 1


def setup(bot):
    bot.add_cog(Store(bot))