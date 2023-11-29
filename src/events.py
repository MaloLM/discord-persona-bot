import discord
from discord.ext import commands
import eventfunctions as event

botPath = "/home/harkinian/scripts/KingBot"

class Events(commands.Cog):
    """
    Cog for handling various events for a Discord bot.
    """

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Listener for on_message event.
        Processes various functions based on the message content.
        """
        if message.author == self.client.user:
            return

        functions = [
            event.ping, # List of events to be loaded 
        ] 

        for function in functions:
            try:
                if await function(self, message):
                    break
            except Exception as e:
                print(f"Error executing event function {function.__name__}: {e}")
                continue  # Continue to the next function if one fails

def setup(client):
    """
    Setup function to add this Cog to the client.
    """
    client.add_cog(Events(client))
