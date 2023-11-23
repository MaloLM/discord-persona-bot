from setuptools import setup, find_packages

# Read dependancies from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    # Name of your package
    name='GPTpersona',

    # Version of your package
    version='0.2.0',

    # Short description
    description='GPTPersona: A Python library for creating interactive, character-driven chat experiences using OpenAI’s GPT API. Designed to simulate conversations with fictional personalities that you define, GPTPersona offers a unique way to engage with AI-driven dialogues, catering to both developers and storytellers looking for a dynamic and creative chatbot experience.',

    # Project URL
    url='https://github.com/MaloLM/GPTpersona',

    # Author and contact
    author='Malo Le Mestre',
    author_email='https://portfolio.dopee.io/#/contact',

    # License
    license='Apache 2.0',

    # Automatically finds all sub-packages
    packages=find_packages(),

    # List of necessary dependencies from requirements.txt
    install_requires=required,

    # Python requires at least this version
    python_requires='>=3.9',

    # Classifiers to help identify key features of your package
    classifiers=[
        'Development Status :: 3 - Alpha',  # For example, Alpha, Beta or Stable
        'Intended Audience :: Developers',   # Target audience
        'License :: OSI Approved :: Apache 2.0 License', # Type of license
        'Programming Language :: Python :: 3.9', # Programming language
    ],

    # Keywords for your package
    keywords='chatbot AI OpenAI GPT GPT-4 interactive-chat character-simulation storytelling fiction dialogue role-play python', 
)
