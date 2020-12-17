import praw
import sqlalchemy
import dataset
import sys

# Used for getting all messages from your inbox and printing them on console, filtered menas it filters comment
# replies from u/Cool down bot
# Add your login info in the following line before runnign
r=praw.Reddit(client_id='[YOUR CLIENT ID]',client_secret='[YOUR CLIENT SECRET]',username='[YOUR ACCOUNT USERNAME]',password='[YOUR ACCOUNT PASSWORD]',user_agent='ShitPissCum1312 1.0 by UniqueUsername0026')

print("Loading, please wait...")
print("\n")
for message in r.inbox.unread(limit=None):
    try:
        author = message.author
        if not(author.name == "CoolDownBot"):
            print("\n")
            try:
                print("From "+author.name)
            except:
                print(" ")

            print(message.subject)
            print(message.body)
            message.mark_read()
    except:
        print(sys.exc_info()[0])
        print("\n")