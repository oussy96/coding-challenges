import os
import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path="config")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'Hello':
            await message.channel.send(f'Hello, {message.author}')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.getenv("TOKEN"))