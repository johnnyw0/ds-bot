import discord
import settings
from discord.ext import commands

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix=settings.PREFIX, help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot Online')
    
    channel = bot.get_channel(892195200984809533)
    await channel.send("tira o hamilton da call urgente")

    await bot.load_extension("cogs.misc.misc")
    print("cog carregada")

@bot.event
async def on_message(message):

    if not message.author.bot:

        if message.content.startswith('bn') or message.content.startswith('Bn') or message.content.startswith('BN'):
            await message.reply('bn')
        if message.content.startswith('bd') or message.content.startswith('Bd') or message.content.startswith('BD'):
            await message.reply('bd')
        if message.content.startswith('bt') or message.content.startswith('Bt') or message.content.startswith('BT') :
            await message.reply('bt')

    await bot.process_commands(message)



bot.run(settings.TOKEN)