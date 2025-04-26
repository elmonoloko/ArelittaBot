import discord
from discord.ext import commands

# Configura los "intents" (permisos del bot)
intents = discord.Intents.default()
intents.message_content = True

# Crea la instancia del bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento que se ejecuta cuando el bot se conecta
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Comando para responder cuando escriben !terriblemala
@bot.command()
async def terriblemala(ctx):
    await ctx.send("¡Este es el comando de prueba de terriblemala!")

# Ejecuta el bot usando el token (pon tu token aquí)
bot.run('TU_TOKEN_AQUI')
