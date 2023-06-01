import os
from dotenv import load_dotenv
import discord
import random
import asyncio

load_dotenv("secrets.env")
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
prefix = "!"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix + 'hola'):
        await message.channel.send('Estoy vivarazooooooooooooooo suuuuuuuuuuu!!!!!!')
    elif message.content.startswith(prefix + 'dado'):
        random_num = random.choice([1, 2, 3, 4, 5, 6])
        await message.channel.send(f'Número aleatorio del dado: {random_num}')
    elif message.content.startswith(prefix + 'fraseSimp'):
        try:
            with open('frases.txt', 'r', encoding='utf-8') as file:
                frases = file.readlines()
                random_frase = random.choice(frases)
                await message.channel.send(random_frase)
        except FileNotFoundError:
            await message.channel.send('No se encontró el archivo de frases.')
    elif message.content.startswith(prefix + 'conquistar'):
        try:
            with open('frases.txt', 'r', encoding='utf-8') as file:
                frases = file.readlines()
                random_frases = random.sample(frases, 20)
                for frase in random_frases:
                    await message.channel.send(frase)
        except FileNotFoundError:
            await message.channel.send('No se encontró el archivo de frases.')
    elif message.content.startswith(prefix + 'que viva el perico'):
        voice_channels = message.guild.voice_channels
        for voice_channel in voice_channels:
            for member in voice_channel.members:
                await member.move_to(random.choice(voice_channels))
    elif message.content.startswith(prefix + 'paseito para'):
        try:
            if len(message.mentions) == 1:
                user = message.mentions[0]
                voice_channels = message.guild.voice_channels
                for _ in range(20):
                    await user.move_to(random.choice(voice_channels))
                    await asyncio.sleep(1)  
                await user.move_to(user.voice.channel) 
            else:
                await message.channel.send('Debes mencionar a un usuario.')
        except AttributeError:
            await message.channel.send('El usuario mencionado no está en un canal de voz.')
    elif message.content.startswith(prefix + 'campeon'):
        try:
            with open('campeones.txt', 'r', encoding='utf-8') as file:
                frases = file.readlines()
                random_frase = random.choice(frases)
                await message.channel.send("tu campeon random: " + random_frase)
        except FileNotFoundError:
            await message.channel.send('no sabe escoger gonorrea')
    elif message.content.startswith(prefix + 'rico gano'):
        await message.channel.send('¡Rico ganó!')
        emojis = ["🎉", "🥳", "🎈", "🎊"]
        for emoji in emojis:
            await message.add_reaction(emoji)

client.run(os.getenv('TOKEN'))