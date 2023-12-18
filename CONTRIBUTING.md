# Contributor's Guide

Thank you for considering contributing to this project. This guide provides information about how to contribute and help make this project better.

## Table of Contents
1. [Setting Up the Development Environment](#setting-up-the-development-environment)
2. [Finding Issues to Work On](#finding-issues-to-work-on)
3. [Creating a Pull Request](#creating-a-pull-request)
4. [Coding Standards](#coding-standards)
5. [Additional Notes](#additional-notes)

## Reporting Issues or Suggesting Improvements

If you encounter any problems or have suggestions for improvements, please feel free to report them in the **Issues** section of this GitHub repository. To ensure efficient and effective communication, please follow these guidelines when submitting an issue:

1. **Use a Clear Title**: Write a concise and informative title for the issue that briefly summarizes the problem or suggestion.

2. **Provide Detailed Information**: In the description, include as much relevant information as possible. This might include:
   - The steps to reproduce the issue (if applicable).
   - The expected outcome versus the actual outcome.
   - Any error messages or screenshots that illustrate the problem.
   - Your environment details, like the operating system and version of the software you are using.

3. **Label Your Issue**: If possible, categorize your issue using labels. Common labels include `bug`, `feature request`, `enhancement`, `documentation`, etc.

4. **Be Respectful and Constructive**: Remember to be respectful and constructive in your communication. We appreciate your contribution to improving this project.

Thank you for helping us make this project better!


## Setting Up the Development Environment

1. **Fork the Repository**: Start by forking [the main repository](https://github.com/MaloLM/Discord-PersonaBot.git).
2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/MaloLM/Discord-PersonaBot.git
   ```
3. **Navigate to the directory**:
   ```bash
   cd Discord-PersonaBot
   ```
4. **Add Upstream Remote**:
   ```bash
   git remote add upstream https://github.com/MaloLM/Discord-PersonaBot.git
   ```
5. **Install Dependencies**:

- Optional: Install PM2 (a Node.js process manager):

  ```
  $ npm install pm2@latest -g
  # or
  $ yarn global add pm2
  ```
- Install the Python dependencies at the project root:

   ```
   pip install -r requirements.txt
   ```

  PM2 helps in managing and keeping your application online.

After completing these steps, your project should be set up and ready to run. Follow any additional setup or configuration instructions specific to the project.



## Creating a Pull Request

1. **Update Your Fork**:
   ```bash
   git fetch upstream
   git merge upstream/main main
   ```
2. **Create a New Branch**:
   ```bash
   git checkout -b branch-name
   ```
3. **Make Your Changes**.
4. **Commit and Push Your Changes**:
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   git push origin branch-name
   ```
5. Navigate to the GitHub page of your fork, and click on "New Pull Request".
6. Ensure the base branch is the main branch of the main repository, and the compare branch is your branch with changes.

## Coding Standards

- Ensure your code is properly formatted.
- Write meaningful commit messages.
- Add comments explaining complex sections of your code.
- Ensure the project builds/tests pass after your changes.

## Additional Notes

- Please be respectful and considerate to other contributors. Adhere to the Code of Conduct.
