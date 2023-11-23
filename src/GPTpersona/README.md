# GPTpersona

## Overview
GPTPersona is a Python library designed for creating interactive, character-driven chat experiences using OpenAI's GPT API. It allows python developpers to simulate conversations with fictional personalities, offering a unique approach to AI-driven dialogues. This library is ideal for developers seeking to create dynamic and creative chatbot experiences.

Initial need to create this library is the implementation of a funny discord bot able to dialogue with discord users [Fun purposes only].

## License
This project is licensed under the Apache 2.0 License. See the [LICENSE](./LICENCE) file for more details.

## Installation
To install GPTPersona, navigate to the root directory of the project and run:
```bash
pip install .
```
For a development setup, use:
```bash
pip install -e .
```

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

## Configuration
Before using GPTPersona, create a `.env` file at the root of the project and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```
Refer to the `.example.env` file for an example of the setup.

## Dependencies
All necessary dependencies are automatically installed through `setup.py`.

## Contributing and Support
For contributions or support, please contact the product owner.

## Connect with project owner

<div> 
   <a href="https://portfolio.dopee.io/#/contact" target="_blank">
      <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=maildotru&logoColor=white" alt="E-mail" height=40>
   </a>
   
   <a href="https://portfolio.dopee.io" target="_blank">
      <img src="https://img.shields.io/badge/Portefolio-green?style=for-the-badge&logo=vuedotjs&logoColor=white" alt="Portefolio" height=40>
   </a>
   
   <a href="https://www.linkedin.com/in/malo-le-mestre/" target="_blank">
      <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin" height=40>
   </a>
</div>

## Features and Limitations
As of now, there are no specific limitations or additional features to highlight. GPTPersona aims to provide a straightforward and effective tool for creating chatbot experiences with fictional characters.
