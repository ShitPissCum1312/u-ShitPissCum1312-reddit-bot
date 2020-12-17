# u-ShitPissCum1312-reddit-bot
### Reddit bot that replies to u/CoolDownBot

This is a Reddit bot that replies to u/CoolDownBot. Written in Python, using PRAW.

# Technical stuff

This bot is written in Python and uses PRAW to communicate with Reddit. To use it you will need your username, password, client ID and client secret. To get client ID and client secret go to https://old.reddit.com/prefs/apps/ and create app. 
**YOU WILL NEED TO MANUALLY EDIT YOUR LOGIN INFO IN EACH INDIVIDUAL SCRIPT BEFORE RUNNING IT**
Scripts use SQLite databases (.db files) and .txt files to store data. Txt files are generated automatically, but you have to manually make .db files. Or you can just leave already existing files and it will run fine.
All script are made and tested on Windows 10 Pro 1709, and I can't say how well it will work on other platforms. PC that used to run this has Intel Celeron E1400 and only 2GB of DDR2 ram and all three main scripts are barely visible in Task Manager, so it should easily run in backgroung on any modern machine.

# How to run

To run you will need Python with the following libraries installed
- praw
- sqlalchemy
- dataset

## Main scripts
Main part of this bot is made out of three scripts: bot.py, mentions.py and replies.py. Those should be different threads of the same process but I didn't know how to make threads in Python when I made this, and I didn't care to fix it. You have to run all three scripts separately in different cmd/terminal windows.

bot.py is the main script and it looks for comments by u/CoolDownBot and replies to them.

mentions.py looks for username mentions and replies to them.

replies.py looks for comment replies and replies to them.

All three of these scripts are made so that if they crash (most of the times due to network error) they restart instead of crashing. This means that doing CTRL+C will restart the script instead of killing it. To kill the script you have to manually close the command prompt (or terminal) window. Again, I know this is not a proper way to do this.

## Other scripts

banned.py is used for getting the list of subreddits you are banned in and adds them to banned.db. This is to prevent your bot from attempting to reply in banned subs and is also useful for avoiding account suspension for ban evasion if you run this on your alt account. All three of the main scripts check banned.db before commenting. It ca also post lists of banned subs and ban messages, more about that explained inside the script itself.

fuck.py is used for spamming a specific post, more explained inside the script.

inbox_filtered.pand inbox_unread.py are used just for printing messages from your inbox on command prompt/terminal, I don't think there is much use for them. I just used them for testing banned.py
