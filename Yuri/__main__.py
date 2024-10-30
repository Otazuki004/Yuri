from discord import *
from Yuri import *
from Yuri.__init__ import Yuri

@Yuri.event
async def on_ready():
	ch = Yuri.get_channel(1301179913885323334)
	await ch.send('I woke up...')

if name == '__main__':
  Yuri.run("MTMwMDc3MzE1NTc0ODQ0NjIyOA.G3-FOg.2lD4_Ce4h_RRowM2kvbaa4W-Gisqf15GAbVYk8")
