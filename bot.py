import discord
from discord.ext import commands
import json
import os

# Charger les paramètres depuis le fichier config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Définir le guild_id comme une variable d'environnement
os.environ['guild_id'] = str(config['guild_id'])

intents = discord.Intents.default()
intents.message_content = True  # Active les intents pour le contenu des messages

bot = commands.Bot(command_prefix="!", intents=intents)

# Charger les cogs
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    # Synchroniser les commandes
    guild = discord.Object(id=config['guild_id'])
    await bot.tree.sync(guild=guild)

# Exécuter le bot
bot.run(config['token'])
