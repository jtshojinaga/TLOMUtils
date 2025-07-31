import discord, logging, logging.handlers
from discord import app_commands
from typing import Literal, Union
from mutations import Mutations, Conditions, AllowedSpecies
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
@app_commands.describe(mutation='The mutation you want to roll for', species="The species you want to roll for. If a species is not listed, it cannot have coat mutations")
async def rollmutations(interaction: discord.Interaction, mutation: Mutations, species: AllowedSpecies):
    """Roll a mutation for your creature"""

    mut = ""
    species = species.name
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

    embed = discord.Embed(
            colour=(discord.Colour.from_str('#f2481d')),
            type='rich',
            title=f'\U0001f3b2 Rolling {mut}')
    # embed.add_field(name='DEBUG', value=f'rand is {rand}, chance is {chance}, val is {suceeded}', inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1379904782587793408/1379909643022893136/IMG_6121.png?ex=687e9980&is=687d4800&hm=0554322a878182f9a4d1e1f9cd7d0aa27d537ee02ef961616fc27077ef1e6530&")

    if(suceeded == None or suceeded == ""):
        embed.add_field(name='No mutation rolled', value=f'Your {species} did not roll a mutation!', inline=True)
    else:
        embed.add_field(name=f'Rolled {suceeded}', value=f'Your {species} rolled **{suceeded}** as a mutation!', inline=True)

    await interaction.response.send_message(embed=embed)

@client.tree.command()
@app_commands.describe()
async def rollconditions(interaction: discord.Interaction):
    """Roll a chronic health condition for your creature"""

    cond = ""
    rand = random.random() * 100
    chance = 0.0
    suceeded = ""

    embed = discord.Embed(
        colour=(discord.Colour.from_str('#f2481d')),
        type='rich',
        title=f'\U0001f3b2 Rolling health conditions')

    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1379904782587793408/1379909643022893136/IMG_6121.png?ex=687e9980&is=687d4800&hm=0554322a878182f9a4d1e1f9cd7d0aa27d537ee02ef961616fc27077ef1e6530&")

    for condition in Conditions:
        cond = condition.name
        chance = condition.value
        if(chance > rand):
            suceeded = cond
            break

    
    if(suceeded == ""):
        embed.add_field(name='No condition rolled', value='You did not roll a health condition!', inline=True)
    else:
        embed.add_field(name=f'Rolled {suceeded.replace("_", " ")}', value=f'You rolled **{suceeded.replace("_", " ")}** as a health condition!', inline=True)
    
    await interaction.response.send_message(embed=embed)

# Disable log handler since we built our own
client.run(token, log_handler=None)
