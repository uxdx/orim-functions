import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()

cred = credentials.Certificate(secrets['FIREBASE_ADMIN_CONFIG'])

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://jinho-337705-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('video')
# snapshot = ref.order_by_child('category').equal_to('Music').get()
# for key in snapshot:
#     print(key)

def category_group(category:str):
    snapshot = ref.order_by_child('category').equal_to(category).get()
    category_video=[]
    for val in snapshot.values():
        category_video.append(val)
    return category_video

def channel_group(channel:str):
    snapshot = ref.order_by_child('channel_name').equal_to(channel).get()
    channel_video=[]
    for val in snapshot.values():
        channel_video.append(val)
    return channel_video

def title_group(title:str):
    snapshot = ref.order_by_child('title').equal_to(title).get()
    title_video=[]
    for val in snapshot.values():
        title_video.append(val)
    return title_video


def Recently_uploadDate(videolist:list):
    a=dict()
    j=0
    for i in videolist:
        a[i['uploadDate']]=j
        j+=1
    b=sorted(a.items(),reverse=True)
    c=[]
    for i in b:
        c.append(i[1])
    d=[]
    for i in c:
        d.append(videolist[i])
    return d

def old_uploadDate(videolist:list):
    a=dict()
    j=0
    for i in videolist:
        a[i['uploadDate']]=j
        j+=1
    b=sorted(a.items(),reverse=False)
    c=[]
    for i in b:
        c.append(i[1])
    d=[]
    for i in c:
        d.append(videolist[i])
    return d

def Recently_category_group(category):
    data=category_group(category)
    video=Recently_uploadDate(data)
    return video

def Recently_channel_group(channel):
    data=channel_group(channel)
    video=Recently_uploadDate(data)
    return video