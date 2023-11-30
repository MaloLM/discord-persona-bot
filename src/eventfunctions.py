import GPTpersona

chat = GPTpersona.Chat()

async def send(self, message):
    """
    Responds to mentions of the bot in Discord messages.
    
    Args:
        message (discord.Message): The Discord message object.
    """
    # Check if the bot is mentioned in the message
    if self.client.user.mentioned_in(message):
        async with message.channel.typing():
            try:
                username = message.author.display_name
                response = chat.send(username, message.content)
                await message.reply(response, mention_author=False)
            except Exception as e:
                # Log the error for debugging purposes
                print(f"Error: {e}")
                await message.reply("Oops, something went wrong.")
                chat.close()  # Close the chat session gracefully
                raise  # Re-raise the exception for further handling if necessary

        return True
