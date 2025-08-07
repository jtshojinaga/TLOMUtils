import discord

def EmbedBuilder(type: str, rolled: str, sucess: bool, value=None):
    """Creates a Discord embed with the specified values according to a format.
    
    Keyword arguments:
    type -- the type of embed (allowed: mut, cond, disease)
    rolled -- the value that was rolled
    sucess -- whether the roll was sucessful or not
    value -- what is being rolled. used only for mutations. (default: None)
    """

    title_string = ""

    match type:
        case "mut":
            if(value is None):
                title_string = f"\U0001f3b2 Rolling all mutations"
            else:
                title_string = f"\U0001f3b2 Rolling {value}"
        case "cond":
            title_string = f"\U0001f3b2 Rolling health conditions"
        case "disease":
            title_string = f"\U0001f3b2 Rolling illnesses"

    if(title_string is ""):
        raise ValueError("Invalid embed type")
    
    embed = discord.Embed(
        colour=(discord.Colour.from_str('#f2481d')),
        type='rich',
        title=title_string
        )

    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1379904782587793408/1379909643022893136/IMG_6121.png?ex=687e9980&is=687d4800&hm=0554322a878182f9a4d1e1f9cd7d0aa27d537ee02ef961616fc27077ef1e6530&")

    if(sucess and type is "mut"):
        embed.add_field(
            name=f'Rolled {rolled}',
            value=f'You rolled **{rolled}** as a mutation!',
            inline=True)
    elif(sucess and type is "cond"):
        embed.add_field(
            name=f"Rolled {rolled}",
            value=f'You rolled **{rolled}** as a health condition!',
            inline=True)
    elif(sucess and type is "disease"):
        embed.add_field(
            name=f"Rolled {rolled}",
            value=f'You rolled **{rolled}** as an illness!',
            inline=True)
    elif(type is "mut"):
        embed.add_field(
            name=f'No mutation rolled',
            value=f'You did not roll a mutation!',
            inline=True)
    elif(type is "cond"):
        embed.add_field(
            name=f'No health condition rolled',
            value=f'You did not roll a health condition!',
            inline=True)
    elif(type is "disease"):
        embed.add_field(
            name=f'No illness rolled',
            value=f'You did not roll an illness!',
            inline=True)
    else:
        raise ValueError("Invalid embed type")

    return embed
