import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")
    print("🔍 Servidores encontrados:")

    for guild in bot.guilds:
        print(f"- {guild.name} | ID: {guild.id}")

    await bot.close()
    
bot.run("SEU_TOKEN_DO_BOT")
