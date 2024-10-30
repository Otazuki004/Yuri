from discord import *
from Yuri import *

@Yuri.event
async def on_ready():
	ch = Yuri.get_channel(1301179913885323334)
	await ch.send('I woke up...')

if __name__ == '__main__':
  Yuri.run('MTMwMDc3MzE1NTc0ODQ0NjIyOA.Gvslhf.Tak40dbpTFbfL1pAPJ-xdoxi1eEmQWVRsY1gQs')
