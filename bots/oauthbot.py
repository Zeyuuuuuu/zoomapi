import sys, os
filename = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(1, filename)
from zoomapi import OAuthZoomClient

import json
from configparser import ConfigParser
from pyngrok import ngrok

parser = ConfigParser()
parser.read("bots/bot.ini")
client_id = parser.get("OAuth", "client_id")
client_secret = parser.get("OAuth", "client_secret")
browser_path = parser.get("OAuth", "browser_path")
print(f'id: {client_id} secret: {client_secret} browser: {browser_path}')

redirect_url = ngrok.connect(4000, "http")
print("Redirect URL is", redirect_url)

client = OAuthZoomClient(client_id, client_secret, redirect_url, browser_path)

user_response = client.user.get(id='me')
user = json.loads(user_response.content)
print(user)
print ('---')

print(json.loads(client.meeting.list(user_id="me").content))
client.chat_channels.list()
channels = json.loads(client.chat_channels.list().content)["channels"]
print(channels)
for c in channels:
    print(c)
    if "Chat Bot Test" in c.values():
        print("Found channel test", c["id"])
        cid = to_channel=c["id"]
stop = False
while not stop:
    print(" ")
    message = input("Enter message: ")
    print(" ")
    if message == "stop":
        stop = True 
    elif message == "help":
        print("stop -- exit")
        print("list -- list all the channels")
        print("create -- create a new channel")
        print("get -- get a channel with id")
        print("update -- update a channel's name with id")
        print("delete -- delete a channel with id")
        print("members -- list all the members of a channel")
        print("invite -- invite new members to channel by emails")
        print("join -- join a channel by id")
        print("leave -- leave a channel by id")
        print("remove -- remove a channel by id")
    elif message == "list":
        print(json.loads(client.chat_channels.list().content))
    elif message == "create":
        channel_name = input("Enter channel name: ")
        channel_type = 1
        email_string = input("Enter members' emails, separated by commas: ")
        email_list = []
        if email_string != "":
            if "," in email_string:
                email_list = email_string.split(",")
            else:
                email_list.append(email_string)
        email_object_list = []
        for email in email_list:
            email_object_list.append({'email':email})
        print(json.loads(client.chat_channels.create(name=channel_name, type=channel_type, members=email_object_list).content))
    elif message == "get":
        channel_id = input("Enter channel id: ")
        print(json.loads(client.chat_channels.get(channelId=channel_id).content))
    elif message == "update":
        channel_id = input("Enter channel id: ")
        channel_name = input("Enter new channel name: ")
        print(client.chat_channels.update(channelId=channel_id, name=channel_name))
    elif message == "delete":
        channel_id = input("Enter channel id: ")
        print(client.chat_channels.delete(channelId=channel_id))
    elif message == "members":
        channel_id = input("Enter channel id: ")
        print(json.loads(client.chat_channels.members(channelId=channel_id).content))
    elif message == "invite":
        channel_id = input("Enter channel id: ")
        email_string = input("Enter members' emails, separated by commas: ")
        email_list = []
        if email_string != "":
            email_list = email_string.split(",")
        email_object_list = []
        for email in email_list:
            email_object_list.append({'email':email})
        print(email_object_list)       
        print(json.loads(client.chat_channels.invite(channelId=channel_id, members=email_object_list).content))
    elif message == "join":
        channel_id = input("Enter channel id: ")
        print(json.loads(client.chat_channels.join(channelId=channel_id).content))
    elif message == "leave":
        channel_id = input("Enter channel id: ")
        print(client.chat_channels.leave(channelId=channel_id))
    elif message == "remove":
        channel_id = input("Enter channel id: ")
        member_id = input("Enter member id: ")
        print(client.chat_channels.remove(channelId=channel_id,memberId=member_id))
    else:
        print(client.chat_messages.post(to_channel=cid, message=message))
