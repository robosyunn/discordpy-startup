from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')
    
@client.event
async def on_message(message):
    # メンバーのリストを取得して表示
    if message.content == '/members':
        print(message.guild.members)
    # 役職のリストを取得して表示
    if message.content == '/roles':
        print(message.guild.roles)
    # テキストチャンネルのリストを取得して表示
    if message.content == '/text_channels':
        print(message.guild.text_channels)
    # ボイスチャンネルのリストを取得して表示
    if message.content == '/voice_channels':
        print(message.guild.voice_channels)
    # カテゴリチャンネルのリストを取得して表示
    if message.content == '/category_channels':
        print(message.guild.categories)    

        

bot.run(token)
