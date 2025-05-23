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

# Obtener el token de las variables de entorno
token = os.getenv("DISCORD_TOKEN_ARELITTA")

# Verifica si el token está disponible
if token is None:
    raise RuntimeError("El token no está definido en las variables de entorno.")
else:
    print("Token cargado correctamente.")

bot.run(token)
