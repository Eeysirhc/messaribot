
from messari_fetch import *

import discord
from discord.ext import commands



client = commands.Bot(command_prefix = '$')
TOKEN = 'YOUR_DISCORD_SECRET_TOKEN_HERE'


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.change_presence(activity = discord.Game("World of Shitecraft"))
 

@client.command()
async def messaribot(ctx, coin):
    coin = coin.upper()
    messari_fetch(coin)
    await ctx.send(file=discord.File(r'/YOUR/FILEPATH/NAME/HERE/toast.png'))

client.run(TOKEN)




