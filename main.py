import discord

class client(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

            client_instance = client()
            client_instance.run('MTM2ODMyNjIwMTgzOTU4MzM2Mg.G-mku1.sHd754fZCCIylah2ofyQgxe94GN8d600_C-qHM')
