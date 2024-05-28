import discord
from discord.ext import commands
import os

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="hello", description="Says hello!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello!")

async def setup(bot):
    await bot.add_cog(Example(bot))
    guild_id = os.getenv('guild_id')
    if guild_id:
        guild = discord.Object(id=int(guild_id))
        bot.tree.add_command(Example(bot).hello, guild=guild)
    else:
        print("Guild ID not found in environment variables.")
