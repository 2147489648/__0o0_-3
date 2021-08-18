import discord
from discord.ext import commands
from core.classes import Cog_Extension
import global_
import json, asyncio

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Bank(Cog_Extension):
    
 
    @commands.command()
    async def money(self, ctx, msg, value:int):
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
              if global_.items[b][0] == global_.inventory[x]:
                embed.add_field(name="Description", value=global_.items[b][1], inline=True)
                embed.add_field(name="Rarity", value=global_.items[b][3], inline=True)
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
    @commands.command()
    async def item_add(self, ctx, item):
      if ctx.author.id == 633082846138990614:
        z = 0
        while len(global_.items) > z:
          if item == global_.items[z][0]:
            embed=discord.Embed(title="Item added", description="You have just successfully added an item to your inventory.", color=0x00ff62)
            embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
            embed.add_field(name="Name", value=global_.items[z][0], inline=True)
            embed.add_field(name="Description", value=global_.items[z][1], inline=True)
            embed.add_field(name="Rarity", value=global_.items[z][3], inline=True)
            embed.add_field(name="Price", value="${}".format(global_.items[z][4]), inline=False)
            embed.set_footer(text="Created by __0o0_#5740")
            await ctx.send(embed=embed)
            global_.inventory.append(global_.items[0][z])
            break
          z += 1
      else:
        await ctx.send('Sorry! You do not have the permission to do this.')
    @commands.command()
    async def item_remove(self, ctx, item):
      if ctx.author.id == 633082846138990614:
        z = 0
        while len(global_.items) > z:
          if item == global_.items[z][0]:
            embed=discord.Embed(title="Item removed", description="You have just successfully removed an item in your inventory.", color=0x00ff62)
            embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
            embed.add_field(name="Name", value=global_.items[z][0], inline=True)
            embed.add_field(name="Description", value=global_.items[z][1], inline=True)
            embed.add_field(name="Rarity", value=global_.items[z][3], inline=True)
            embed.add_field(name="Price", value="${}".format(global_.items[z][4]), inline=False)
            embed.set_footer(text="Created by __0o0_#5740")
            await ctx.send(embed=embed)
            global_.inventory.remove(global_.items[z][0])
            break
          z += 1
      else:
        await ctx.send('Sorry! You do not have the permission to do this.')
    @commands.command()
    async def item_use(self, ctx, item, num:int):
      if ctx.author.id == 633082846138990614:
        z = 0
        while len(global_.items) > z:
          if item == global_.items[z][0]:
            embed=discord.Embed(title="Item/Items uesd", description="You have just successfully used {} item/items in your inventory.".format(num), color=0x00ff62)
            embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
            embed.add_field(name="Name", value=global_.items[z][0], inline=True)
            embed.add_field(name="Description", value=global_.items[z][1], inline=True)
            embed.add_field(name="Rarity", value=global_.items[z][3], inline=True)
            embed.add_field(name="Price", value="${}".format(global_.items[z][4]), inline=False)
            embed.set_footer(text="Created by __0o0_#5740")
            await ctx.send(embed=embed)
            u = 0
            while num > u and item == global_.items[z][0]:
              global_.inventory.remove(global_.items[z][0])
              u += 1
              await asyncio.sleep(global_.items[z][2]*60)
              embed=discord.Embed()
              embed.add_field(name="Duration ended", value='The duration of the item "{}" is ended.'.format(global_.items[z][0]), inline=False)
              await ctx.send(embed=embed)
            break
          z += 1
      else:
        await ctx.send('Sorry! You do not have the permission to do this.')


def setup(bot):
    bot.add_cog(Bank(bot))