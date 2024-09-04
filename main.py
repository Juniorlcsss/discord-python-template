import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Connected to Discord as {self.user}!')

intents = discord.Intents.default()
intents.message_content = True

#gets token from the token.txt file
with open("token.txt") as file:
    token = file.read()


client = Client(intents=intents)
client.run(token)