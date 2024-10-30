from discord import Intents
from discord.ext import commands
import logging

logging.basicConfig(
    format="[Yuri] %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

intents = Intents.default()
intents.message_content = True 

Yuri = commands.Bot(command_prefix="!", intents=intents)
