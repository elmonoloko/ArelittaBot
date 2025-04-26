import os
from discord.ext import commands
from discord import Intents

intents = Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

token = os.getenv("DISCORD_TOKEN_ARELITTA")
if token is None:
    raise RuntimeError("El token no está definido en las variables de entorno.")

bot.run(token)
