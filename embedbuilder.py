import discord

def EmbedBuilder(type: str, rolled: str, sucess: bool, value=None):
    """Creates a Discord embed with the specified values according to a format.
    
    Keyword arguments:
    type -- the type of embed (allowed: mut, cond, disease, skin, gender)
    rolled -- the value that was rolled
    sucess -- whether the roll was sucessful or not
    value -- what is being rolled. used only for mutations and skins. (default: None)
    """

    title_string = ""
    emoji_icon = f"\U0001f3b2"  # \U0001f3b2 is the Unicode value for a dice emoji; shown in titles
    watermark_emoji = f"\U0001F409"  # \U0001F409 is the unicode for a dragon; shown in watermark

    # The emojis must be in the format of a Python Unicode value! Google the name of the emoji you want plus "unicode"
    # You should get a value like U+1f49 or some other format
    # Add \ to the front, and replace the + with as many 0s as necessary to make the part after the U 8 characters long
    # so U+1f49 -> \U00001F49 

    match type:
        case "mut":
            if(value is None):
                title_string = f"{emoji_icon} Rolling all mutations"
            else:
                title_string = f"{emoji_icon} Rolling {value}"
        case "cond":
            title_string = f"{emoji_icon} Rolling health conditions"
        case "disease":
            title_string = f"{emoji_icon} Rolling illnesses"
        case "skin":
            title_string = f"{emoji_icon} Rolling skins"
        case "gender":
            title_string = f"{emoji_icon} Rolling gender"

    if(title_string == ""):
        raise ValueError("Invalid embed type")
    
    embed = discord.Embed(
        colour=(discord.Colour.from_str('#f2481d')),
        type='rich',
        title=title_string
        )

    embed.set_thumbnail(
        url="https://cdn.discordapp.com/attachments/1379904782587793408/1379909643022893136/IMG_6121.png?ex=687e9980&is=687d4800&hm=0554322a878182f9a4d1e1f9cd7d0aa27d537ee02ef961616fc27077ef1e6530&")

    if(sucess and type == "mut"):
        embed.add_field(
            name=f'Rolled {rolled}',
            value=f'You rolled **{rolled}** as a mutation!',
            inline=True)
    elif(sucess and type == "cond"):
        embed.add_field(
            name=f"Rolled {rolled}",
            value=f'You rolled **{rolled}** as a health condition!',
            inline=True)
    elif(sucess and type == "disease"):
        embed.add_field(
            name=f"Rolled {rolled}",
            value=f'You rolled **{rolled}** as an illness!',
            inline=True)
    elif(type == "skin"):
        embed.add_field(
            name=f"Rolled {rolled}",
            value=f'{value}\n\nYour creature will use the **{rolled}** skin!',
            inline=True)
    elif(type == "gender"):
        embed.add_field(
            name=f"Rolled {rolled}",
            value=f'Your creature should be a **{rolled}**!',
            inline=True)
    elif(type == "mut"):
        embed.add_field(
            name=f'No mutation rolled',
            value=f'You did not roll a mutation!',
            inline=True)
    elif(type == "cond"):
        embed.add_field(
            name=f'No health condition rolled',
            value=f'You did not roll a health condition!',
            inline=True)
    elif(type == "disease"):
        embed.add_field(
            name=f'No illness rolled',
            value=f'You did not roll an illness!',
            inline=True)
    else:
        raise ValueError("Invalid embed type")

    # Edit the text of the footer here
    # If you don't want a footer, place a # in front of the line to comment it out
    embed.set_footer(text=f"{watermark_emoji} The Land of Mordor")

    return embed
