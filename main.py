import os
import discord
import datetime
import logging
import requests
from urllib.parse import *
import sys
from threading import Thread


prefix = os.getenv('PREFIX')
#if not os.path.exists(f'./{datetime.date.today()}'.replace('-', '_')):
#    os.mkdir(f'./{datetime.date.today()}'.replace('-', '_'))
#logging.basicConfig(
#    filename=f'./{datetime.date.today()}'.replace('-', '_') +
#    f'/message_loging_{datetime.datetime.now()}.txt',
#    filemode='a',
#    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#    datefmt='%H:%M:%S',
#    level=logging.INFO)
client = discord.Client()


@client.event
async def on_ready():
    print(f"Logged in as: {client.user}")
    #logging.info(msg=f'Logged in as:{client.user}\twith ID:{client.user.id}')


@client.event
async def on_message(message):
    #logging.info(msg=str(
    #    str(message.author.id) + ' : ' + str(message.author.name) + " : " +
    #    message.content))
    if client.user in message.mentions:
        await message.channel.trigger_typing()
        data = (requests.get(
            f'http://api.brainshop.ai/get?bid=168343&key=TnWck9uCIp23y9vJ&uid={message.author.id}&msg={quote_plus(message.content)}'
        ))
        parsed = data.text
        parsed = parsed.replace('false', 'False').replace('false','False')
        print(dict(eval(parsed)))
        parsed = dict(eval(parsed))
        await message.reply(parsed["cnt"])


client.run(os.getenv("TOKEN"))
