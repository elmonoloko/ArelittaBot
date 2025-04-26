import os
import discord
from discord.ext import commands

# Configura los "intents"
intents = discord.Intents.default()
intents.message_content = True

# Crea el bot
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def terriblemala(ctx):
    await ctx.send("¡Este es el comando de prueba de terriblemala!")

# Ejecutar el bot con el token desde una variable de entorno
bot.run(os.getenv('MTM2NTQ5ODQ0MzY5ODUzNjUyOQ.GUfFYR.9VdnzHSbkKqKi7T8oEdA2UKARpJE0apNsbmTj8'))
