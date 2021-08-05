import discord
import json, asyncio
import global_
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Quest(Cog_Extension):
    @commands.command()
    async def quest(self, ctx, msg, msg2):
      if ctx.author.id == 633082846138990614:
        if msg == 'list':
          if msg2 == 'all':
            b = 0
            while len(global_.quest[0]) > b:
              embed=discord.Embed(title="Quest information:", color=0x00b3ff)
              embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
              embed.set_thumbnail(url=global_.quest[4][b])
              embed.add_field(name="Quest type", value=global_.quest[0][b], inline=False)
              embed.add_field(name="Quest name", value=global_.quest[1][b], inline=False)
              embed.add_field(name="Quest time", value="{} mins".format(global_.quest[2][b]), inline=False)
              embed.add_field(name="Quest reward", value="${}".format(global_.quest[3][b]), inline=False)
              embed.set_footer(text="Created by __0o0_#5740")
              await ctx.send(embed=embed)
              b += 1
          else:
            b = 0
            while len(global_.quest[0]) > b:
              if msg2 == global_.quest[0][b]:
                embed=discord.Embed(title="Quest information:", color=0x00b3ff)
                embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
                embed.set_thumbnail(url=global_.quest[4][b])
                embed.add_field(name="Quest type", value=global_.quest[0][b], inline=False)
                embed.add_field(name="Quest name", value=global_.quest[1][b], inline=False)
                embed.add_field(name="Quest time", value="{} mins".format(global_.quest[2][b]), inline=False)
                embed.add_field(name="Quest reward", value="${}".format(global_.quest[3][b]), inline=False)
                embed.set_footer(text="Created by __0o0_#5740")
                await ctx.send(embed=embed)
                b += 1
              else:
                b += 1
        elif msg == 'finished':
          x = 0
          while len(global_.quest[0]) > x:
            if global_.quest[1][x] == msg2:
              embed=discord.Embed(title="Quest finished", description="Congratulations! You completed a quest.", color=0x00ff62)
              embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
              embed.set_thumbnail(url=global_.quest[4][x])
              embed.add_field(name="Quest type", value=global_.quest[0][x], inline=False)
              embed.add_field(name="Quest name", value=global_.quest[1][x], inline=False)
              embed.add_field(name="Reward", value="${}".format(global_.quest[3][x]), inline=False)
              embed.set_footer(text="Created by __0o0_#5740")
              await ctx.send(embed=embed)
              global_.score += global_.quest[3][x]
              await ctx.send('You have ${} now!'.format(global_.score))
              break
            x += 1
        elif msg == 'started':
          y = 0
          while len(global_.quest[0]) > y:
            if global_.quest[1][y] == msg2:
              embed=discord.Embed(title="Quest started", description="You started a quest.", color=0x00b3ff)
              embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
              embed.set_thumbnail(url=global_.quest[4][y])
              embed.add_field(name="Quest type", value=global_.quest[0][y], inline=False)
              embed.add_field(name="Quest name", value=global_.quest[1][y], inline=False)
              embed.add_field(name="Quest duration", value="{} mins".format(global_.quest[2][y]), inline=False)
              embed.add_field(name="Quest reward", value="${}".format(global_.quest[3][y]), inline=False)
              embed.set_footer(text="Created by __0o0_#5740")
              await ctx.send(embed=embed)
              await asyncio.sleep(global_.quest[2][y]*60)
              embed=discord.Embed(title="Quest finished", description="Congratulations! You completed a quest.", color=0x00ff62)
              embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
              embed.set_thumbnail(url=global_.quest[4][y])
              embed.add_field(name="Quest type", value=global_.quest[0][y], inline=False)
              embed.add_field(name="Quest name", value=global_.quest[1][y], inline=False)
              embed.add_field(name="Reward", value="${}".format(global_.quest[3][y]), inline=False)
              embed.set_footer(text="Created by __0o0_#5740")
              await ctx.send(embed=embed)
              global_.score += global_.quest[3][y]
              await ctx.send('You have ${} now!'.format(global_.score))
              break
            y += 1
      else:
        await ctx.send('Sorry! You do not have the permission to do this.')

'''
    @commands.command()
    async def questcreate(self, ctx, quest_type, quest_name, quest_description, quest_score):
        if ctx.author.id == 633082846138990614:
            embed=discord.Embed(title="The quest *{}* was successfully created.".format(quest_name), description="Description: {}".format(quest_description), color=0x00b3ff)
            embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
            embed.add_field(name="Quest type", value=quest_type, inline=True)
            embed.add_field(name="Reward", value=quest_score, inline=True)
            embed.set_footer(text="Created by __0o0_#5740")
            await ctx.send(embed=embed)
'''
def setup(bot):
  bot.add_cog(Quest(bot))