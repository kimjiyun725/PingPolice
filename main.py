import asyncio
from decouple import config
import discord
from discord.ext import commands
import os

description = '''A bot that keeps track of users who delete their message after @\'ing Valorant. '''
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents, description=description)

def is_owner(ctx):
    print(ctx.author, type(ctx.author))
    if str(ctx.author) == config('owner', default=''):
        return True
    return False

@bot.command()
async def load(ctx, extension):
    if is_owner(ctx):
        await bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    if is_owner(ctx):
        await bot.unload_extension(f'cogs.{extension}')
    
@bot.command(name='reload')
async def reload_extension(ctx, extension):
    if is_owner(ctx):
        await bot.unload_extension(f'cogs.{extension}')
        await bot.load_extension(f'cogs.{extension}')
        
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
        
if __name__ == '__main__':
    asyncio.run(load_extensions())
    TOKEN = config('TOKEN', default='')
    bot.run(TOKEN)