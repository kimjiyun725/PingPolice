from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Hello is online.')
        
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello!')
        
async def setup(bot):
    print('Hello module loaded in.')
    await bot.add_cog(Hello(bot))

async def teardown(bot):
    print('Hello module unloaded.')
    await bot.remove_cog(Hello(bot))
    