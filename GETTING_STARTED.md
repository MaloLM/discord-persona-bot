# Getting started

## Environment Setup

- **Development Operating System**: The project was tested on Raspbian 5.10.103-v7+ and MacOS 14.1.1 (Sonoma).

- **Python Version**: Ensure Python 3.9(.9) is installed for compatibility.

## Process Management with PM2

If you wish to use PM2 for managing your application, follow these steps:

- **PM2 Overview:**
  - PM2 is a process manager for Node.js applications that offers features like continuous application running, efficient logging, system monitoring, and hot reloading.
  - It is compatible with JavaScript and can be installed using either NPM or Yarn.

- **Installation:**
  - To install PM2, use one of the following commands:
    - Using NPM:
      ```bash
      npm install -g pm2
      ```
    - Using Yarn:
      ```bash
      yarn global add pm2
      ```

- **Configuration:**
  - Before using PM2, you'll need to configure the `/src/conf/app.config.js` file to prepare for execution with PM2.
  - Ensure the following attributes are correctly set in the `app.config.js` file:
    - The `interpreter` attribute should be configured with the path to the desired Python interpreter (use the `which python` command to find it).
    - The `cwd` attribute should contain the absolute path to the directory where the `main.py` file to be executed is located.

- **Starting the Application with PM2:**
  - Once PM2 is installed and your configuration is set, you can start your application using the following PM2 command:
    ```bash
    pm2 start directory_to_app.config.js 
    ```

For more detailed information on setting up and using PM2, refer to the [PM2 Quick Start Guide](https://pm2.keymetrics.io/docs/usage/quick-start/).

Feel free to customize this README section to fit your project's specific details and requirements.


- **Environment File**:
    - Create a `.env` file in the `/src` directory.
    - This file should be structured according to the `.example.env` template provided in the project.

### Alternative Process Management Options

While PM2 is the recommended process management tool, there are alternative methods available, especially for users who prefer different setups:

- **systemctl (Linux Systems)**: 
    - For Linux users, `systemctl` can be an effective alternative for managing the application's processes. 
    - It provides system-level control and is well-suited for managing background services.

- **Direct Python Execution**:
    - As a simpler approach, users can directly run the application by executing `/src/main.py` using Python.
    - This method is straightforward but may lack advanced features like automatic restarts and logging provided by dedicated process managers.

Regardless of the chosen method, ensure that it aligns with your system capabilities and management preferences.

## Installation

### Python Dependencies

- The file `/requirements.txt` lists all the necessary libraries for the proper functioning of the Python application. 
- To install these dependencies, run `pip install -r /requirements.txt` in your terminal.
- This will ensure that your environment is equipped with all the required Python packages to run the application smoothly.

(Expand this section with detailed installation instructions. Include steps like cloning the repository, setting up the environment, and running the bot.)


## OpenAI Service Setup

1. **Create an OpenAI Developer Account**: Sign up for a developer account at [OpenAI](https://openai.com).

2. **Access Account Management**: Navigate to your account management interface [Here](https://platform.openai.com/docs/overview).

3. **Generate an API Key**:
    - In the "API Keys" menu, generate a new secret API key. Ensure that it is stored securely.
    - Copy the API Key and place it in the `/src/.env` file of your application.

4. **Fund Your Account**:
    - Load credits into your account via the "Settings/Billing" menu by selecting "Add credit to balance".

5. **Select and Set Up the GPT Model**:
    - Choose the desired GPT model from the [API documentation](https://platform.openai.com/docs/models/models).
    - Set the selected GPT model in the `/src/.env` file of your application.


## Discord Developer Portal Setup (2023)

1. **Create a Discord Account**: If you don't have one already, sign up at [Discord](https://discord.com).

2. **Access the Developer Portal**: Log in to the Discord Developer Portal at [https://discord.com/developers](https://discord.com/developers).

3. **Create a New Application**: Use the dedicated button to create a new application. Name your application and agree to Discord's terms of service, then click 'Create'.

4. **Bot Configuration**:
    - Navigate to the "Bot" menu and reset the token to receive a new one.
    - Copy this secret token and place it in the `/src/.env` file of your app.
    - In the Developer Portal, you can customize your bot's attributes such as profile image, description, and permissions.

5. **Set Up Privileged Gateway Intents**:
    - In the "Bot" menu under "Privileged Gateway Intents", enable the following permissions and then save:
        - PRESENCE INTENT
        - SERVER MEMBERS INTENT
        - MESSAGE CONTENT INTENT

6. **Generate OAuth2 URL**:
    - In the "OAuth2" / "URL Generator" menu, enable the following scopes:
        - bot
        - applications.commands
    - This will generate an invitation link for the bot. Copy this link.
    
    Using the invitation link, you can invite the bot to any server where you have server management permissions.

For more information about how to setup a Discord bot, check the [Discord Dev portal documentation](https://discord.com/developers/docs/intro).


## Persona Setup / Prompt Engineering

The character's response capability can be customized in the following file: `/src/GPTpersona/persona.py`.

You can edit the value of `INIT_PROMPT` to define the bot's behaviors and responses.

As this is based on the GPT model, the bot is trained to generate content that is politically correct.

You can improve the prompt through iterations and trial and error. Let your imagination run wild!

To customize the bot's persona and responses, follow these steps:

1. Navigate to the `/src/GPTpersona/persona.py` file in your app directory.

2. Locate the `INIT_PROMPT` variable in the file and modify its value to specify the desired persona or behavior for your bot.

3. Save the changes to the `persona.py` file.

4. Test the bot's responses by interacting with it using the modified persona.