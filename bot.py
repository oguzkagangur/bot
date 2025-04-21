import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def mem(ctx):
    resim = random.choice(os.listdir("images"))
    with open(f'images/{resim}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

#prefix koyulsun. sonra belirlediğimiz komut ismi oılsun. bu yazılınca bot bize genel çevreyle ilgili öneri veya bilgi versin

oneriler = ["Pet şişeleri süs eşyasına çevirebilirsiniz.","Çöpleri geri dönüşüm kutularına ayrıştırabiliriz.", "Geri dönüşüme uygun olmayan çöpleri normal çöp kutusuna atabilirsiniz.", "Çöplerin yer atılmaması gerekir."]


@bot.command()
async def kirlilik(ctx):
    await ctx.send(random.choice(oneriler))

bot.run("TOKEN")
