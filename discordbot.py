from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='!ap ')
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
    await ctx.send('APEXキルレ0.3の会botだよ〜\n> コマンドリスト\n> `!ap hello` : 挨拶をするよ〜\n> `!ap help`  : 今表示しているやつだよ\n> `!ap info`  : 案内を表示するよ〜\n')

@bot.command()
async def info(ctx):
    rep = f'ようこそ!APEXキルレ0.3サーバーへ！\n\n> \n> **システム**カテゴリの**プラットフォーム選択**よりプラットフォームが選択できるよ！\n> \n> **全般**カテゴリより**id交換**のチャンネルに :origin_id: *ORIGIN ID*または :ps_id: *PD ID*をかくとid交換できるかも！？！？'
    await ctx.send(rep)

@bot.command()
async def sakai(ctx):
    rep = f'*sakai*はだめです！！！だめですオワコン。おわおわり。'
    awiat ctx.send(rep)
    
#@bot.event
#async def on_message(message):
#   if message.content.startswith('!ap add '):
#        args = message.content.split()
#        unm  = message.author.mentions
#        uid  = args[2]
#        CHANNEL_ID = 680449983425675280
#        channel = bot.get_channel(CHANNEL_ID)  
#        rep = f'{unm} {uid}'
#        await channel.send(rep)
#        
#   elif bot.user in message.mentions:
#        reply = f'{message.author.mention} なにかお困りでしたら`!ap helps`とタイプしてみてね！'
#        await message.channel.send(reply) # 返信メッセージを送信

@bot.event
async def on_member_join(member):
    rep = f'{member.mention} ようこそ!APEXキルレ0.3サーバーへ！\n\n> \n> **システム**カテゴリの**プラットフォーム選択**よりプラットフォームが選択できるよ！\n> \n> **全般**カテゴリより**id交換**のチャンネルに :origin_id: *ORIGIN ID*または :ps_id: *PD ID*をかくとid交換できるかも！？！？'
    CHANNEL_ID = 680045070438629380
    channel = bot.get_channel(CHANNEL_ID)  
    await channel.send(rep)
    
bot.run(token)
