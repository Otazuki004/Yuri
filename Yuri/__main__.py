from discord import *
from Yuri import *
import asyncio

@Yuri.event
async def on_ready():
    ch = Yuri.get_channel(1301179913885323334)
    await ch.send('I woke up...')

async def start():
    await load_mods()

if __name__ == '__main__':
    asyncio.run(start())
    Yuri.run(TOKEN)
