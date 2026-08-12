This is my repository for various *personal* projects related to World of Warcraft.

As of 2026/08/12, this folder contains two major projects:


## Raider.io applicant look-up (Main project)

Scripts to look up and rank every applicant for my WoW dungeon- or raid groups, inspired by OP.GG for LoL.

**To get started**, run 'main.py' or open 'websitetest.html' for a nice GUI.

A json of each applicant (generated via the Raider.io addon) is manually copy-pasted into the "input.json" file, and each player profile will then be looked up on raider.io.

Rankings include Player name, Role, Class, missing enchant/gem counter, iLvl, CE/AOTC achievement count, KSM count, Best run, m+ Score, completion timers, recent runs, and Age (time since last run). There are also a score breakdown for each dungeon.

See the below image for an example of what the website looks like.

![Image link](images/web_preview.png)

And if run via the terminal, here is what the terminal output looks like.

![Image link](images/showcase.PNG)


## Warcraftlog analysis and summary

Scripts to look up every M+ player you've played with throughout a WoW season to see what rank they ended up at. It will also generate a summary of your journey,
providing statistics over how many attempts / groups you needed for each of your M+ keys.

**How to use:**, run 'logrun_rio_integration.py' or 'logrun.py' (to generate a summary with or without end-of-season player scores, respectively).

Because logs cannot be easily sraped automatically (due to captchas), we instead have to open each log on the warcraftlog website and Ctrl+A Ctrl+C everything that is visible in the browser into a .txt file in the logged_runs folder. This repo already contains some of my old logs, so for demo purposes this step can be skipped.

See this image for a screenshot of what the summary looks like.

![Image link](images/web_preview.png)
