from GPTpersona.gpt import Gpt
import GPTpersona.persona as persona

class Chat:
    """
    Chat class to interface with a GPT-based chat model.
    This class initializes the chat model with a preset prompt and provides
    a method to send messages to the chat model and receive responses.
    """

    def __init__(self) -> None:
        """
        Initializes the Chat instance with a preset prompt and a GPT model.
        """
        self.initial_prompt = persona.INIT_PROMPT
        self.gpt_model = Gpt(self.initial_prompt)

    def send(self, username: str, message: str) -> str:
        """
        Sends a message to the GPT model and receives a response.

        Args:
            username (str): The username of the person sending the message.
            message (str): The message text to send.

        Returns:
            str: The response from the GPT model.
        """
        response = self.gpt_model.complete_chat(message, "user", username)
        return response
    
    def close(self):
        del(self.gpt_model)

