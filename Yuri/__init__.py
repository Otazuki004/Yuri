import discord
from discord.ext import commands
import logging
import os

logging.basicConfig(
    format="[Yuri] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.members = True 

TOKEN = os.getenv('TOKEN')
Yuri = commands.Bot(command_prefix="!", intents=intents)
