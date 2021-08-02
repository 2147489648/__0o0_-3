import discord
import json
import global_
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Quest(Cog_Extension):
    @commands.command()
    async def createquest(self, ctx, quest_type, quest_name, quest_description, quest_score):
        if ctx.author.id == 633082846138990614:
            embed=discord.Embed(title="The quest *{}* was successfully created.".format(quest_name), description="Description: {}".format(quest_description), color=0x00b3ff)
            embed.set_author(name="Hi! I am __0o0_'s Robot.", icon_url="https://i.pinimg.com/originals/6e/53/5b/6e535b2f01ffb2daa02b6072a908a2a2.jpg")
            embed.add_field(name="Quest type", value=quest_type, inline=True)
            embed.add_field(name="Reward", value=quest_score, inline=True)
            embed.set_footer(text="Created by __0o0_#5740")
            await ctx.send(embed=embed)
            
def setup(bot):
  bot.add_cog(Quest(bot))