from discord.ext import commands

class PingReply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("PingReply is online.")
    
    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.author == self.bot.user:
            return
        if not ctx.role_mentions:
            return
        for mention in ctx.role_mentions:
            if mention.name != 'Valorant':
                return
        
        print(ctx.role_mentions[0].name)
        # response = self.bot.user + ': ' + ctx.content
        print(type(self.bot.user.name))
        await ctx.channel.send(content= ctx.content, reference=ctx)

async def setup(bot):
    print('PingReply module loaded in.')
    await bot.add_cog(PingReply(bot))
    
async def teardown(bot):
    print('PingReply module unloaded.')
    await bot.remove_cog(PingReply(bot))