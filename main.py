import discord
from discord.ext import commands
import random, os, requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot . command ()
async def checkAI(ctx):
    if ctx.message. attachments:
        for file in ctx.message.attachments:
            namafile = file.filename
            utlfile = file.url
            await file. save(f'./ {namafile} ')
            await ctx. send(f'gambar telah disimpan dengan nama {namafile}')

            # KLASIFIKASI DAN INFERENSI
            kelas, skor = get_class('keras_model.h5', 'label.txt', namafile)

            if kelas == 'airbus\n' and skor >= 0.75:
                await ctx.sent('ini pesawat airbus')
                await ctx.sent('teknologi pesawat lebih maju')
            elif kelas == 'boeing\n' and skor >= 0.75:
                await ctx.sent('ini pesawat boeing')
                await ctx.sent('mesin pesawat lebih bagus')
            else:
                await ctx.sent('ini bukan pesawat airbus atau boeing')
    
    else:
        await ctx.send('mana nih gaambarnya??????')

bot.run("token")
