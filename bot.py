import discord
from discord.ext import commands
import os

# Intents = permissões que o bot usa no Discord
intents = discord.Intents.default()
intents.message_content = True  

# Define o prefixo dos comandos, ex: !help
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot logado como {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! Estou online.")

# ⚠️ O token você NÃO vai deixar fixo aqui
# Vamos puxar de uma variável de ambiente
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    print("❌ ERRO: Configure a variável DISCORD_TOKEN no ambiente!")
else:
    bot.run(TOKEN)
