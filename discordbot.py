from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!ap03 ')
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
async def helps(ctx):
    await ctx.send('APEXキルレ0.3の会botだよ〜\n> コマンドリスト\n> `!ap03 hello` : 挨拶をするよ〜\n> `!ap03 help`  : 今表示しているやつだよ\n> `!ap03 info`  : 案内を表示するよ〜\n')

@bot.command()
async def info(ctx):
    rep = f'ようこそ!APEXキルレサーバーへ！\n> **システム**カテゴリの**プラットフォーム選択**よりプラットフォームが選択できるよ！\n> **全般**カテゴリより**id交換**のチャンネルに*oringin*または*ps*をかくとid交換できるかも！？！？'
    await ctx.send(rep)
    
@bot.event
async def on_member_join(member):
    rep = f'{member.mention} ようこそ!APEXキルレサーバーへ！\n> **システム**カテゴリの**プラットフォーム選択**よりプラットフォームが選択できるよ！\n> **全般**カテゴリより**id交換**のチャンネルに*oringin*または*ps*をかくとid交換できるかも！？！？'
    await member.send(rep)
    
bot.run(token)
