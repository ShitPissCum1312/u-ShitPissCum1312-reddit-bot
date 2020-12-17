import praw
import sqlalchemy
import dataset
import sys
import os
import time
from datetime import datetime

# This is the main script that looks for comments by u/CoolDownBot and replies to them
# Before running you must add your login info on line 16

db = dataset.connect('sqlite:///databasename.db')
bandb = dataset.connect('sqlite:///banned.db')

# Add your login info here before running. User agent can be anythig, or you can leave this one
r=praw.Reddit(client_id='[YOUR CLIENT ID]',client_secret='[YOUR CLIENT SECRET]',username='[YOUR ACCOUNT USERNAME]',password='[YOUR ACCOUNT PASSWORD]',user_agent='ShitPissCum1312 1.0 by UniqueUsername0026')

print("Initializing log.txt")
logfile = open("log.txt","a")
logfile.close()
print("Starting")
while True:
    try:
        print("Started")
        comm = "Hello you fucking bot. \n\n My fucking name is fucking ShitPissCum1312 and I am a fucking bot fucking made by some fucking mother-fuckung-fucker who was really fucking annoyed by your fucking comments with a fucking purpose of fucking telling you to fucking shut the fuck up. What the fucking fuck are you even fucking trying to fucking achieve by fucking doing this fucking shit fucking over and fucking over? No fucking one is fucking going to fucking stop fucking saying fucking fuck just because you fucking told them so. \n\n Fuck you all and have a nice fucking day. [Fuck.](https://www.youtube.com/watch?v=ukznXQ3MgN0)"
        
        # This one got me suspension for violent content so I do not recommend using it
        comm1 = "Hello you fucking bot. \n\n My fucking name is fucking ShitPissCum1312 and I am about to fucking tell you a fucking story. \n\n Once upon a fucking time, there was a fucking fucker who fucking fucked everything in fucking sight. Eventually, the fucking townspeople got fucking sick of his fucking antics and fucking decided to fucking teach the depraved fucker a fucking lesson. \n\n \"Fuck, I fucking hate this fucking fucker!\" Said the mayor's fucking assistant. \n\n \"That's why we're fucking going to fucking kill him,\" said the fucking mayor. \n\n \"Fuck yeah, we are!\" Replied the fucking assistant. \n\n So, the fucking mayor, the fucking assistant, and even the fucking townspeople concocted a fucking brilliant plan to make that fuckwit rapist get what he fucking deserves. \n\n In the center of the fucking town, they put a big, beautiful fucking diamond right underneath the fucking founder's fucking statue, hiding behind their houses, waiting for that fucker to take the fucking bait. \n\n Eventually, he fucking showed up, immediately fucking noticing the gorgeous fucking gem under the fucking statue. And as fucking expected, he fucking slinked his creepy fucking ass over to the fucking stone to perform his fucked up molestation. \n\n But then, he noticed something was fucking wrong. He began to feel as if the fucking skin of his fucking dick was fucking burning off. Then he realized. \n\n **The diamond was laced with fucking acid.** \n\n The terrible fucking toxin's effects began to immediately fucking spread across his whole fucking body, eventually reaching his fucking insides. \n\n His fucking screams could be heard from across the fucking river, even by the nearby fucking town. \n\n The fuckwit was fucking eaten alive by the fucking acid, and the fucking townspeople fucking rejoiced. They had a huge fucking party to fucking celebrate their fucking accomplishment. \n\n And since then, no one ever had to fucking worry about that dipshit fucking their fucking valuables ever fucking again. \n\n **~The Fucking End~** \n\n \n\n I fucking hope you fucking liked this fucking story. Fuck you all and have a nice fucking day. [Fuck.](https://www.youtube.com/watch?v=ukznXQ3MgN0)"


        for comment in r.redditor('CoolDownBot').stream.comments():
            try:
                cbody = comment.body
            except:
                sub = "error no sub"
            try:
                sub = comment.subreddit.display_name
            except:
                sub = "error no body"
            if bandb['banned'].find_one(subname=sub) == None:
                if db['replied_to'].find_one(comment_id=comment.id) == None:
                    try:
                        now=datetime.utcnow()
                        datetimestr = now.strftime("%Y-%m-%dT%H:%M:%S")
                        print("Replying in "+sub+" "+datetimestr+"UTC")
                        print(comment.body)
                        print("\n")
                        comment.reply(comm)
                        db['replied_to'].insert(dict(comment_id=comment.id))
                    except:
                        print(sys.exc_info()[0])
                        print("\n")
                else:
                    print("Already replied to")
                    print(comment.body)
                    print("\n")
            else:
                print("Banned in "+sub)
    except:
        print("An error occured")
        now=datetime.utcnow()
        datetimestr = now.strftime("%Y-%m-%dT%H:%M:%S")
        print("Writing to log.txt")
        logfile = open("log.txt","a")
        logfile.write("\n "+datetimestr+"UTC bot.py ")
        logfile.close()
        print("Attempting to restart")