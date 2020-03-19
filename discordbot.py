from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!ap03')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def hello(ctx):
    await ctx.send('Hello! Apexキルレ0.3の会botだよ〜')

@bot.command()
async def show_members(ctx):
    await ctx.send(message.guild.members)

bot.run(token)
