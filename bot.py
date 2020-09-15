import os
import discord
import ethos_origin_generator

TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DISCORD_PREFIX') or '%%'

PLAYING_STATUS= os.getenv('PLAYING_STATUS') or f'{PREFIX}stellarisGenOrigin'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print(f'Here\'s an invite link for you to use: https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot')
    playing_status = discord.Game(name=PLAYING_STATUS)
    await client.change_presence(status=discord.Status.idle, activity=playing_status)

@client.event
async def on_message(message):
    if message.content.startswith(f'{PREFIX}stellarisGenOrigin'):
        ethos, origin, gestalt = ethos_origin_generator.generate()
        ethoses = '\n'.join(f'**{k}**: {v}' for k, v in ethos.items() if v != 0)
        msg = f'Origin: `{origin}`\n\nEthoses:\n{ethoses}\n\nGestalt: `{gestalt}`'
        await message.channel.send(msg)
    elif message.content.startswith(f'{PREFIX}help'):
        await message.channel.send(f'Help:\n`{PREFIX}stellarisGenOrigin` - generates stellaris ethos and origin info\n`{PREFIX}help` - shows this')
        

client.run(TOKEN)
