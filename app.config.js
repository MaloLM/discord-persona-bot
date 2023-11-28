module.exports = {
    apps : [{
      name   : "personaBot",
      script : "./main.py",
      interpreter: 'To Be Configured', // TBD
      cwd: 'To Be Configured', // the directory from which your app will be launched // TBD
      watch: true,
      ignore_watch: ['conf','__pycache__','GPTpersona'] // Ignore hot reloading as you wish
    }]
  }

  // PM2 documentation: https://pm2.keymetrics.io/docs/usage/quick-start/
