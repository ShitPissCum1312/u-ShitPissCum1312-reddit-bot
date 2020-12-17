import praw
import sqlalchemy
import dataset
import sys
import os
import time
from datetime import datetime, timedelta

# This script checks your inbox for ban messages, extracts subs and adds them to SQLite database and text file.
# SQLite database (banned.db) is used by other scripts to avoid trying to reply in banned subs anc can also be useful for avoiding
# account suspensions for ban evasion if you run this on alt account
# Text files (banned.txt and banmsg.txt) are used for posting banned subs and ban messages. To do this you have to
# first manually create two text submissions and then add their IDs, submission to banmsgsubm and
# comment to banmsgsubm (lines 24 and 29).
# DO NOT FORGET TO ADD YOUR LOGIN INFO IN LINE 20

db = dataset.connect('sqlite:///banned.db')

# Add your login info before running. User agent can be anything or even keep this
r=praw.Reddit(client_id='[YOUR CLIENT ID]',client_secret='[YOUR CLIENT SECRET]',username='[YOUR ACCOUNT USERNAME]',password='[YOUR ACCOUNT PASSWORD]',user_agent='ShitPissCum1312 1.0 by UniqueUsername0026')
r.validate_on_submit = True

# Add your banned subs submission ID here
bansubm=r.submission(id="ipgkho")

# banmsgcomm=r.comment(id="g4tx4ja") NOT USED

# Add your ban messages submission ID here
banmsgsubm=r.submission(id="jmr445")

now=datetime.utcnow()
datetimestr = now.strftime("%Y-%m-%dT%H:%M:%S")
banfile=open("banned.txt","w")
banfile.write("Fucking updated on "+datetimestr+"UTC \n\n")
banfile.close()
banmsgfile=open("banmsg.txt","w")
banmsgfile.write("Fucking ban messages (for fucking subs that fucking provided the fucking ban messages instead of just generic fucking \"You have been banned\"): \n\n")
banmsgfile.close()

print("Loading, please wait...")
print("\n")
print("You have been fucking banned from the following fucking subreddits")
print("\n")
n=0
total=0
for message in r.inbox.all(limit=None):
    msg=message.body
    if "You have been permanently banned from participating" in msg:
        type=" - Permanent fucking ban: \n\n"
        substr=msg.split("r/",1)[1]
        sub=substr.split(".")[0]
        if db['banned'].find_one(subname=sub) == None:
            db['banned'].insert(dict(subname=sub))
            n=n+1
        msgdateunix=message.created_utc
        msgdate=datetime.fromtimestamp(msgdateunix) # returns UTC+2 instead of UTC, check this before running
        msgdatefixed= msgdate - timedelta(hours=2, minutes=0)
        msgdatestr=msgdatefixed.strftime("%Y-%m-%dT%H:%M:%S")
        print("r/"+sub+" - Permanently banned on "+msgdatestr+"UTC")
        banfile=open("banned.txt","a")
        banfile.write("r/"+sub+" - Permanently fucking banned on "+msgdatestr+"UTC \n\n")
        banfile.close()
        total=total+1
        if "Note from the moderators:" in msg:
            bmsgstr=msg.split("Note from the moderators:",1)[1]
            bmsg=bmsgstr.split("If you have a question regarding your ban,")[0]
            print("r/"+sub+type+bmsg+" \n\n\n\n")
            banmsgfile=open("banmsg.txt","a")
            banmsgfile.write("r/"+sub+type+bmsg+" \n\n\n\n")
            banmsgfile.close()
            
    elif "You have been temporarily banned from participating" in msg:
        type=" - Temporary fucking ban: \n\n"
        substr=msg.split("r/",1)[1]
        sub=substr.split(".")[0]
        if db['banned'].find_one(subname=sub) == None:
            db['banned'].insert(dict(subname=sub))
        msgdateunix=message.created_utc
        msgdate=datetime.fromtimestamp(msgdateunix) # returns UTC+2 instead of UTC, check this before running
        msgdatefixed= msgdate - timedelta(hours=2, minutes=0)
        msgdatestr=msgdatefixed.strftime("%Y-%m-%dT%H:%M:%S")
        print("r/"+sub+" - Temporarily banned on "+msgdatestr+"UTC")
        banfile=open("banned.txt","a")
        banfile.write("r/"+sub+" - Temporarily fucking banned on "+msgdatestr+"UTC \n\n")
        banfile.close()
        if "Note from the moderators:" in msg:
            bmsgstr=msg.split("Note from the moderators:",1)[1]
            bmsg=bmsgstr.split("If you have a question regarding your ban,")[0]
            print("r/"+sub+type+bmsg+" \n\n\n\n")
            banmsgfile=open("banmsg.txt","a")
            banmsgfile.write("r/"+sub+type+bmsg+" \n\n\n\n")
            banmsgfile.close()
print("\n")
print("Total "+str(total)+" subs permabanned, "+str(n)+" since last checked")
banfile=open("banned.txt","a")
banfile.write("Total "+str(total)+" fucking subs permabanned, "+str(n)+" since last fucking check \n\n")
banfile.close()
print("Update Reddit submission?(y/n)")
asd=input()
if((asd=="y") or (asd=="Y")):
    print("Updating submission...")
    banfile=open("banned.txt","r")
    submbody=banfile.read()
    bansubm.edit(submbody)
    banfile.close()
    print("Submission edited")


print("Update ban messages?(y/n)")
asasas=input()
if((asasas=="y") or (asasas=="Y")):
    print("Updating comment...")
    banmsgfile=open("banmsg.txt","r")
    commentbody=banmsgfile.read()
    banmsgfile.close()
    banmsgsubm.edit(commentbody)
    print("Edited, press any key to exit...")
    askljdfh=input()