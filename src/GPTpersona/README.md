# GPTpersona

## Overview
GPTPersona is a Python library designed for creating interactive, character-driven chat experiences using OpenAI's GPT API. It allows python developpers to simulate conversations with fictional personalities, offering a unique approach to AI-driven dialogues. This library is ideal for developers seeking to create dynamic and creative chatbot experiences.

Initial need to create this library is the implementation of a funny discord bot able to dialogue with discord users [Fun purposes only].

## Usage
To get started with GPTPersona, check out the `basic_usage.py` example in the `/examples` directory. Here's a quick snippet:

```python
from gptpersona import Chat

def main():
    chat = Chat()
    persona_answer = chat.send("Zelda", 'Mais père ?')
    print("Persona answer: ", persona_answer)
    chat.close()

if __name__ == "__main__":
    main()
```

This example demonstrates how to initiate a chat session, send a message, and receive a response.