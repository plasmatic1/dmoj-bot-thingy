from discord.ext import commands


def register_commands(bot: commands.Bot):
    @bot.command()
    async def echo(ctx: commands.Context):
        await ctx.channel.send(f'Hi {ctx.message.content}, I\'m dad!')
