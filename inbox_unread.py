import praw
import sqlalchemy
import dataset
import sys

# Prints all unread messages on console
# Add your login info in the following line before running

r=praw.Reddit(client_id='[YOUR CLIENT ID]',client_secret='[YOUR CLIENT SECRET]',username='[YOUR ACCOUNT USERNAME]',password='[YOUR ACCOUNT PASSWORD]',user_agent='ShitPissCum1312 1.0 by UniqueUsername0026')

print("Loading, please wait...")
print("\n")
for message in r.inbox.unread(limit=None):
    author = message.author
    print("\n")
    try:
        print("From "+author.name)
    except:
        print(" ")

    print(message.subject)
    print(message.body)
    message.mark_read()