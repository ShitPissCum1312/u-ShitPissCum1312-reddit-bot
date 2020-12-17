import praw
import sqlalchemy
import dataset
import sys
import os
import time
from datetime import datetime

# Replies to comment replies. Add your login info in line 15 before running

db = dataset.connect('sqlite:///commreply.db')
bandb = dataset.connect('sqlite:///banned.db')

# Add your login info here before running
r=praw.Reddit(client_id='[YOUR CLIENT ID]',client_secret='[YOUR CLIENT SECRET]',username='[YOUR ACCOUNT USERNAME]',password='[YOUR ACCOUNT PASSWORD]',user_agent='ShitPissCum1312 1.0 by UniqueUsername0026')

print("Initializing log.txt")
logfile = open("log.txt","a")
logfile.close()
print("Starting")
while True:
    try:
        print("Started")
        print("\n")
        for reply in praw.models.util.stream_generator(r.inbox.comment_replies):
            try:
                user=reply.author.name
                body=reply.body
                sub=reply.subreddit.display_name
            except:
                user="[ERROR NO USER]"
                body="[ERROR NO BODY]"
                sub="[ERROR NO SUB]"
            if bandb['banned'].find_one(subname=sub) == None:
                if ((not "CoolDownBot" in user) and (not "profanitycounter" in user) and (not "SNSAleksandarVucic" in user) and (not "AutoModerator" in user) and (not "FecesUrineSpermACAB" in user) and (not "EmojiPoliceGetDown" in user) and (not "dankestmemestar" in user) and (not "AvoidBot" in user) and (not "SubSimGPT2Interactive" in sub)):
                    if db['commreply'].find_one(rep=reply.id) == None:
                        try:
                            now=datetime.utcnow()
                            datetimestr = now.strftime("%Y-%m-%dT%H:%M:%S")
                            print("From "+user+" in "+sub+" "+datetimestr+"UTC")
                            print(body)
                            if((" cum" in body) or (" Cum" in body) or (" shit" in body) or (" Shit" in body)): # This got me suspension for harrasment, I recommend removing this IF ad always replying default reply (the one in ELSE part)
                                reply.reply("I just fucking shit and cum. \n\n **FUCKING FAQ** \n\n **What the fuck does this mean?** \n\n The amount of fucking shit (and cum) on my fucking computer and floor has fucking increased by one. \n\n **Why the fuck did you fucking do this?** \n\n There are several fucking reasons I may deem a fucking comment to be fucking worthy of fucking feces or ejaculation. These include, but are not fucking limited to: \n\n *Being fucking gay \n\n *Dank fucking copypasta bro, where'd you fucking find it \n\n *fucking walter \n\n **Am I going to fucking shit and cum too?** \n\n No - not yet. But you should fucking refrain from fucking shitposting and cumposting like this in the fucking future. Otherwise I will be forced to fucking shit and cum again, which may fucking put your fucking shitting and cumming privileges in fucking jeopardy. \n\n **I don't fucking believe my fucking comment deserved being fucking shit and cum at. Can you fucking un-cum it?** \n\n Sure, mistakes fucking happen. But only in fucking exceedingly rare fucking circumstances will I put fucking shit back into my fucking butt. If you would fucking like to issue an fucking appeal, fucking shoot me a hot fucking load explaining what the fuck I fucking got wrong. I tend to fucking respond to retaliatory ejaculation within several fucking minutes. Do fucking note, however, that over 99.9% of semen fucking dies before it can fucking fertilize the fucking egg, and yours is likely no fucking exception. \n\n **How the fuck can I fucking prevent this from fucking happening in the fucking future?** \n\n Accept the fucking goopy brown and white substance and move on. But learn from this fucking mistake: your fucking behavior will not be fucking tolerated in my mom's fucking basement. I will continue to fucking shit and cum until you fucking improve your fucking conduct. Remember: ejaculation is a fucking privilege, not a fucking right.")
                            else: # I recommend removing the IF part and always replying with this one
                                reply.reply("Hi u/"+user+" and thanks for fucking replying to my fucking comment. I am a fucking bot so I have no fucking idea what the fuck I am supposed to fucking do but my fucking owner might fucking see this fucking comment so he should fucking know what the fuck he is supposed to do, so thanks anyway. \n\nFuck you all and have a nice fucking day. [Fuck.](https://www.youtube.com/watch?v=ukznXQ3MgN0)")
                            db['commreply'].insert(dict(rep=reply.id))
                            print("\n")
                            repfile = open("replies.txt","a")
                            repfile.write("From "+user+" in r/"+sub+" id="+reply.id+" "+datetimestr+"UTC")
                            repfile.write("\n")
                            repfile.write(body)
                            repfile.write("\n")
                            repfile.write("\n")
                            repfile.close()
                        except:
                            print(sys.exc_info()[0])
                            print("\n")
                            repfile = open("replies.txt","a")
                            repfile.write("An exception occured while writing to file, most probably UnicodeEncodeError. Comment could not be written to file")
                            repfile.write("\n")
                            repfile.write("\n")
                            repfile.close()
                    else:
                        print("Already replied to")
                        print("From "+user)
                        print(body)
                        print("\n")
            else:
                print("Banned in "+sub)
    except:
        print("An error occured")
        now=datetime.utcnow()
        datetimestr = now.strftime("%Y-%m-%dT%H:%M:%S")
        print("Writing to log.txt")
        logfile = open("log.txt","a")
        logfile.write("\n "+datetimestr+"UTC replies.py ")
        logfile.close()
        print("Attempting to restart")