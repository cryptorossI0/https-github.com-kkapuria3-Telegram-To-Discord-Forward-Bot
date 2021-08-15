import yaml
import sys
import logging
import discord

''' 
------------------------------------------------------------------------
    DISCORD CLIENT - Init the client
------------------------------------------------------------------------
'''

discord_client = discord.Client()
with open('config.yml', 'rb') as f:
    config = yaml.safe_load(f)

''' 
------------------------------------------------------------------------
    MESSAGE AS WE RECIEVE FROM FORWARDGRAM SCRIPT
------------------------------------------------------------------------
'''

message = sys.argv[1]

''' 
------------------------------------------------------------------------
    DISCORD SERVER START EVENT - We will kill this immaturely
------------------------------------------------------------------------
'''
# when discord is initalized, it will trigger this event. 
# we quickly send messages to our discord channels and quit the script prematurely.
# this gets trigged again when a new message is sent on channel from telegram

@discord_client.event
async def on_ready():

    print('We have logged in as {0.user}'.format(discord_client))
    print('Awaiting Telegram Message')

    # My channels are for RTX card drops and PS5
    channel_3080 = discord_client.get_channel(config["discord_3080_channel"])
    channel_3070 = discord_client.get_channel(config["discord_3070_channel"])
    channel_3060 = discord_client.get_channel(config["discord_3060_channel"])
    channel_PS5 = discord_client.get_channel(config["discord_PS5_channel"])

    if '3080' in message:
        await channel_3080.send(message)
    elif '3070' in message:
        await channel_3070.send(message)
    elif '3060' in message:
        await channel_3060.send(message)
    elif 'Sony' in message:
        await channel_PS5.send(message)

    quit()

discord_client.run(config["discord_bot_token"])

    

    

