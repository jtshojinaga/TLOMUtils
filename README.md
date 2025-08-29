# TLOM Utility
Version 3.0.0 

Author: enver.gortash on Discord 

Permissions: You may not use, reproduce, or distribute any part of this code outside of the author's GitHub page and the TLOM staff discussions.  

## About the Server
The Land of Mordor (TLOM) is a fan-made community server for the game Path of Titans focused on modded fantasy-style creatures and realism-based roleplay. You can join here: https://discord.gg/tlom

## About the Bot

TLOM Utility (TLOMUtils) is a Discord bot designed to provide members with a more realistic, chance-based system for making their characters including coat mutations like albinism and health conditions. This creates a more immersive roleplay experience and keeps the in-game ecosystem balanced.

# Features
- Integrates with Discord's built-in application commands (AKA "slash commands") via the discord.py library to create a seamless user experience
- TLOMUtils has a brand-new, re-worked configuration system, making it easier than ever to adjust the rates of mutations, the infectiousness of disease, and more!
- Using a custom EmbedBuilder class, messages can be sent using a fully customizable embed, including a logo and a footer

## Commands
- `/rollmutations`: Rolls a random mutation for various coat mutations either individually or all at once.
- `/rollconditions`: Rolls a random health condition from a list, ranging from mild conditions like colorblindness to severe conditions like a weak immune system.
- `/rollillness`: Rolls a random acute illness for player to roleplay being sick from wounds, rotten meat, etc.
- `/rollskin`: Rolls a random skin from player-provided genetics based on their parents.
- `/rollgender`: Rolls a gender for a player's creature, featuring a toggle for advanced mode. Advanced mode adds additional options, like high-testosterone female and low-testosterone male to the pool of available choices, allowing more customization.

# Setup

## config.json

This file is probably the one you will get familiar with, as it contains all of the information about how likely certain things are to occur. 
The words in "quotes" are the names, and what will show up on Discord. The numbers represent percentages, so 10.0 -> 10% chance of happening.
You can add your own values in any order you want, so long as you follow the format! If you need help, https://jsonchecker.com/ can help
format your JSON correctly. 

A note about mutations:
The mutation code is different than the rest of the code. A mutation MUST be present in both config.JSON and mutations.PY, or else the bot will not
work and will not roll that mutation. You also cannot remove the "all" value, or else users can't roll for all mutations at once

## mutations.py

The only time you need to be here is if you're adding another mutation. Just make sure to follow the instructions at the top of the file,
and you should be good to go.

## embedbuilder.py

This is the part of the program that makes all the bot replies look nice and pretty in an embed.
You can change things like the icon that appears in the title, the text or emoji in the watermark, the thumbnail image, and the color of the embed.
All of these things have comments explaining how to edit them. Don't touch anything else, or else things may get ugly (literally).

