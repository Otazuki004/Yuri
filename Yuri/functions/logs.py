from subprocess import getoutput as r
from discord import File, Embed
from discord.ext import commands
from Yuri.decorator.filter_user import filter_user

@filter_user('otazuki')
async def log_cmd(ctx, *args, **kwargs):
    stats = await ctx.reply('Loading...')
    log = r('tail log.txt')
    await stats.delete()
    embed = Embed(title='Log output', description=f"```python\n{log}```", color=0xFF0000)
    await ctx.reply(embed=embed)

async def setup(Yuri):
    for name in ['log', 'logs']:
        Yuri.add_command(commands.Command(log_cmd, name=name))
