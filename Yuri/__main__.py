from discord import *
from Yuri import *
import asyncio

async def on_ready():
    ch = Yuri.get_channel(1301179913885323334)
    await ch.send('I woke up...')

async def start():
    await load_mods()
    await on_ready()

if __name__ == '__main__':
    Yuri.loop.create_task(start())
    Yuri.run(TOKEN)
