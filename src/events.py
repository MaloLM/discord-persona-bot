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
        self.switch = self._load_switch()

    def _load_switch(self):
        """
        Loads the switch configuration from a file.
        """
        try:
            with open(f"{botPath}/conf/switch.txt", "r") as switchEvent:
                return switchEvent.read()
        except IOError as e:
            print(f"Error loading switch file: {e}")
            return ""

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        Listener for on_message event.
        Processes various functions based on the message content.
        """
        if message.author == self.client.user or str(message.guild.id) not in self.switch:
            return

        functions = [
            event.ping, event.vxtwitter, event.votre_majeste, event.leaf, 
            event.riso, event.coiffeur, event.je_suis, event.random_quote, 
            event.chaine
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
