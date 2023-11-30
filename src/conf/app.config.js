module.exports = {
    apps : [{
      name   : "personaBot",
      script : "main.py",
      interpreter: '/Users/malo/Documents/projets/informatique/github/Discord-PersonaBot/venv/bin/python',
      cwd: '/Users/malo/Documents/projets/informatique/github/Discord-PersonaBot/src/', // the directory from which your app will be launched
      watch: true,
      ignore_watch: ['conf','__pycache__','GPTpersona'] // Ignore hot reloading as you wish
    }]
  }

  // PM2 documentation: https://pm2.keymetrics.io/docs/usage/quick-start/
