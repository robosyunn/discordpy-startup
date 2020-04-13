from discord.ext import commands
import os
import traceback

# bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()


@client.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command()
async def neko(ctx):
    await ctx.send('にゃーん')


@client.command()
async def aho(ctx):
    await ctx.send('にょーん')


@client.command()
async def 月曜日(ctx):
    await ctx.send('数学A　体育　政治経済')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')


client.run(token)
