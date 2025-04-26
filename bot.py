import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Asegúrate de que el token provenga de la variable de entorno
bot.run(os.getenv("DISCORD_TOKEN"))
