import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
import pytz

class Gpt:
    """
    Gpt class for interfacing with the OpenAI GPT model.
    Handles the initialization of the model and message processing.
    """

    def __init__(self, system_msg: str) -> None:
        """
        Initializes the GPT model with a system message.

        Args:
            system_msg (str): Initial system message to configure the model.
        """
        # Environment setup
        env_path = Path(__file__).resolve().parents[4] / '.env'
        load_dotenv(dotenv_path=env_path)

        # Timezone setup
        paris_tz = pytz.timezone('Europe/Paris')
        self.current_time = datetime.now(paris_tz).strftime('%Y-%m-%d %H:%M:%S')

        # Model setup
        self.model = "gpt-4-1106-preview"
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        # Initial system message preparation
        reinforced_system_msg = f'First instruction: always answer in JSON format and specify it. {system_msg}'
        self.messages = [{"role": "system", "content": reinforced_system_msg}]

    def complete_chat(self, input_message: str, role: str, username: str) -> str:
        """
        Processes an input message and returns the GPT model response.

        Args:
            input_message (str): The message to be processed.
            role (str): The role of the message sender (e.g., 'user').
            username (str): The username of the message sender.

        Returns:
            str: The response from the GPT model.
        """
        # Format the input message with user information and local time
        if role == "user":
            input_message = f"User {username} says: {input_message}; Local time: {self.current_time}"

        # Append the message to the conversation history
        self.messages.append({"role": role, "content": input_message})

        # Get response from the model
        response = self.client.chat.completions.create(
            model=self.model,
            response_format={"type": "json_object"},
            messages=self.messages
        )
        assistant_response = json.loads(response.choices[0].message.content)['response']

        # Append the assistant's response and log the conversation
        self.messages.append({"role": "assistant", "content": assistant_response})
        self._log_conversation()

        return assistant_response

    def _log_conversation(self):
        """
        Logs the conversation history to a file.
        """
        with open("/home/harkinian/scripts/KingBot/GPTpersona/api/openai/kingLogs.txt", "a") as log_file:
            log_file.write(f"{self.messages} -> {len(self.messages)}\n\n")
