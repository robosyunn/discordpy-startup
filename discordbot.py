from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')


@bot.command()
async def aho(ctx):
    await ctx.send('にょーん')


@bot.command()
async def 月曜日(ctx):
    await ctx.send('数学A　体育　政治経済')


# @bot.event
# async def on_message(message):
#     if message.author.bot:
#         return
#     if message.content == '/あいうえお':
#         await message.channel.send('かきくけこ')


bot.run(token)
