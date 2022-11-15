# This example requires the 'message_content' intent.
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):  
    # if the user (message.author) is the bot (client.user), return so it does not loop forever
    if message.author == client.user:
        return
    
    if message.role_mentions:
        print(message.role_mentions)
        role = message.role_mentions[0]
        print(role)
        print(role.id)
        await message.channel.send(content=response, reference=message)