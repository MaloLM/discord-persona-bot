import os
import discord
from random import choice
from dotenv import load_dotenv
from discord.ext import commands

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configure intents for the bot
intents = discord.Intents.default()
intents.members = True
intents.presences = True
intents.message_content = True
intents.guilds = True

# Initialize the bot
client = commands.Bot(command_prefix='k!', intents=intents)

# List of extensions to load
extensions = ['events']

@client.event
async def on_ready():
    """
    Event handler for when the bot becomes ready.
    It sets a random status from the given list of activities.
    """
    print(f'{client.user.name} has connected to Discord!')
    
    activities = [
        "Playing a game", # For example
        "Listenning to music", # Add more for more diversity...
    ]
    chosen_activity = choice(activities)
    await client.change_presence(activity=discord.Game(chosen_activity))

# Main entry point
if __name__ == '__main__':

    # Load extensions
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print(f'Extension {extension} cannot be loaded. [{error}]')

    # Run the bot
    client.run(TOKEN)
