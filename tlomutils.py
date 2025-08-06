import discord, logging, logging.handlers
from discord import Embed, app_commands
from typing import Literal, Union
from mutations import Mutations, Conditions, Illnesses
from embedbuilder import EmbedBuilder
import random

# Declaring intents
intents = discord.Intents.default()
intents.message_content = True

# Enabling custom logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,
    backupCount=3,)

frmt = '%Y - %m - %d, %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}',
                              frmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Guilds list
guilds = [discord.Object(id=1324790404385734717)]

# Setting up Client config & token
token = '${{ secrets.BOT_TOKEN }}'
class MyClient(discord.Client):
    def __init__(self):
        super().__init__(
            intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        for id in guilds:
            self.tree.copy_global_to(guild=id)
            await self.tree.sync(guild=id)

client = MyClient()

game = discord.Game(
        'The Land of Mordor', 
        platform='Path of Titans')

# Logging in as bot
@client.event
async def on_ready():
    print(f'Successful login: {client.user}')
    await client.change_presence(activity=game)

# Commands
@client.tree.command()
async def ping(interaction: discord.Interaction):
    """Replies with pong"""
    await interaction.response.send_message('Pong!')

@client.tree.command()
@app_commands.describe(mutation='The mutation you want to roll for')
async def rollmutations(interaction: discord.Interaction, mutation: Mutations):
    """Roll a mutation for your creature"""

    mut = ""
    rand = random.random() * 100
    chance = 0.0
    suceeded = ""

    if (mutation.name == 'all'):
        mut = 'all mutations'
        for mutation in Mutations:
            if(mutation.value > rand):
                suceeded = mutation.name
                break
            else:
                suceeded = None
    else:
        mut = mutation.name
        chance = mutation.value
        if(chance > rand):
            suceeded = mut
        else:
            suceeded = None

    if(suceeded == None or suceeded == ""):
        embed = EmbedBuilder(type='mut', value=mut, sucess=False)
    else:
        embed = EmbedBuilder(type='mut', value=mut, sucess=True)

    await interaction.response.send_message(embed=embed)

@client.tree.command()
@app_commands.describe()
async def rollconditions(interaction: discord.Interaction):
    """Roll a chronic health condition for your creature"""

    cond = ""
    rand = random.random() * 100
    chance = 0.0
    suceeded = ""

    for condition in Conditions:
        cond = condition.name
        chance = condition.value
        if(chance > rand):
            suceeded = cond
            break

    if(suceeded == ""):
        embed = EmbedBuilder(type='cond', value=None, sucess=False)
    else:
        embed = EmbedBuilder(type='cond', value=suceeded.replace("_", " "), sucess=True)

    await interaction.response.send_message(embed=embed)

@client.tree.command()
@app_commands.describe()
async def rollillness(interaction: discord.Interaction):
    """Roll an acute illness for your creature"""
    cond = ""
    rand = random.random() * 100
    chance = 0.0
    suceeded = ""

    for illness in Illnesses:
        cond = illness.name
        chance = illness.value
        if(chance > rand):
            suceeded = cond
            break

    if(suceeded == ""):
        embed = EmbedBuilder(type='disease', value=None, sucess=False)
    else:
        embed = EmbedBuilder(type='disease', value=suceeded.replace("_", " "), sucess=True)

    await interaction.response.send_message(embed=embed)


# Disable log handler since we built our own
client.run(token, log_handler=None)
