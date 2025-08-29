import discord, logging, logging.handlers # allows us to build our own logger
from discord import app_commands # required to use / commands
import json # needed to read config file
import random # required for rolling
from typing import Optional # allows arguments to be optional
from mutations import Mutations
from embedbuilder import EmbedBuilder # makes building the reply embed easier

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

# Setting up config
file = open('config.json')
data = json.load(file)
token = data["token"]

# sorts by lowest value, so rarer items are rolled first
# this guarantees that lower chance items will be rolled for every time
# though they may not be chosen!
mutations_dict = dict(sorted(data["mutations"].items(), key=lambda item: item[1]))
conditions = dict(sorted(data["conditions"].items(), key=lambda item: item[1]))
illnesses = dict(sorted(data["illnesses"].items(), key=lambda item: item[1]))
genders = dict(sorted(data["genders"].items(), key=lambda item: item[1]))
file.close()

# Setting up Client config
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
        'The Land of Mordor')

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
    """Rolls a random mutation for your creature"""
    
    mut = ""
    rand = random.random() * 100
    chance = 0.0
    suceeded = ""

    if(mutation.name == 'all'):
        mut = 'all mutations'
        for item in mutations_dict:
            if(mutations_dict.get(item) > rand):
                suceeded = item
                break
            else:
                suceeded = None
    else:
        mut = mutation.name
        chance = mutations_dict.get(mut)
        if(chance > rand):
            suceeded = mut
        else: suceeded = None

        print(mut)
    
    if((suceeded is None or suceeded == "") and mut == "all mutations"):
        embed = EmbedBuilder(type='mut', rolled=suceeded, sucess=False)
    elif(suceeded is None or suceeded == ""):
        embed = EmbedBuilder(type='mut', rolled=mut, sucess=False, value=mut)
    else:
        embed = EmbedBuilder(type='mut', rolled=suceeded, sucess=True, value=mut)

    await interaction.response.send_message(embed=embed)

@client.tree.command()
async def rollconditions(interaction: discord.Interaction):
    """Roll a chronic health condition for your creature"""

    cond = ""
    rand = random.random() * 100
    chance = 0.0
    suceeded = ""

    for item in conditions:
        cond = item
        chance = conditions.get(item)
        if(chance > rand):
            suceeded = cond
            break

    if(suceeded == ""):
        embed = EmbedBuilder(type='cond', rolled=None, sucess=False)
    else:
        embed = EmbedBuilder(type='cond', rolled=suceeded, sucess=True)

    await interaction.response.send_message(embed=embed)

@client.tree.command()
async def rollillness(interaction: discord.Interaction):
    """Roll an acute illness for your creature"""
    cond = ""
    rand = random.random() * 100
    chance = 0.0
    suceeded = ""

    for item in illnesses:
        cond = item
        chance = illnesses.get(item)
        if(chance > rand):
            suceeded = cond
            break

    if(suceeded == ""):
        embed = EmbedBuilder(type='disease', rolled=None, sucess=False)
    else:
        embed = EmbedBuilder(type='disease', rolled=suceeded, sucess=True)

    await interaction.response.send_message(embed=embed)

@client.tree.command()
@app_commands.describe(
    motherdom="The dominant skin of your creature's mother", 
    fatherdom="The dominant skin of your creature's father",
    recessives="Other skins to roll separated by commas (eg. cinnabar,borealis,redtail)")
async def rollskin(interaction: discord.Interaction, motherdom: str, fatherdom: str, recessives: str):
    """Pick a skin from parents' genetics. At least one recessive is required"""

    motherdom = motherdom.capitalize()
    fatherdom = fatherdom.capitalize()

    dom_weight = 30 # the weight you want dominant skins to have; eg, how often a dominant skin should be chosen

    recessives = recessives.title()
    skins = recessives.split(",")

    skins.append(motherdom)
    skins.append(fatherdom)
    skins.reverse() # to make it easier to match the weights up correctly
    
    weights = [dom_weight, dom_weight]

    num = len(skins)-2
    while num > 0:
        weights.append((100-(dom_weight*2)) / len(skins)-2) # if dom_weight is 30, evaluates to 40 divided by the number of recessives
        num -= 1

    chosen = random.choices(skins, cum_weights=weights, k=1)[0]

    embed = EmbedBuilder(type="skin", rolled=chosen.capitalize(), 
                         sucess=True, value=f"Dominants: {motherdom} \U000000D7 {fatherdom}\nRecessives: {recessives.replace(",", ", ")}")
    await interaction.response.send_message(embed=embed)

@client.tree.command()
@app_commands.describe(advanced="Advanced mode includes additional gender options besides male and female. Default: False")
async def rollgender(interaction: discord.Interaction, advanced: Optional[bool]):
    """Choose a gender for your creature"""

    sex = ""

    if(advanced is None or advanced is False):
        # only include male & female
        sex = random.choice(["female", "male"])
    else:
        # include advanced gender options
        sex = random.choices( 
            list(genders.keys()), 
            weights=list(genders.values()), 
            k=1)[0] # random.choices() returns a list so we have to get the value out

    embed = EmbedBuilder(type="gender", rolled=sex, sucess=True)
    await interaction.response.send_message(embed=embed)



# Disable log handler since we built our own
client.run(token, log_handler=None)