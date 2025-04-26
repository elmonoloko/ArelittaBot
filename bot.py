import os
from discord.ext import commands
from discord import Intents

# Configura los intents
intents = Intents.default()
intents.members = True  # Para recibir eventos de miembros
intents.message_content = True  # Para recibir el contenido de los mensajes

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Asegúrate de que el token provenga de la variable de entorno correcta
bot.run(os.getenv("DISCORD_TOKEN_ARELITTA"))
