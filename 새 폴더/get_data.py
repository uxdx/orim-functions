import pyrebase
import json
from search import Recently_category_group, Recently_channel_group
from search_al import search_title, search_channel_name

with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()
config = secrets['FIREBASE_CONFIG']
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# 메인 페이지용 함수
def get_index_data() -> dict:
    videos_Gaming = db.child('mostPopular').child('Gaming').get()
    videos_list = videos_Gaming.val()
    videos_Music = db.child('mostPopular').child('Music').get()
    videos_list2 = videos_Music.val()
    videos_Sports = db.child('mostPopular').child('Sports').get()
    videos_list3 = videos_Sports.val()
    videos_list.update(videos_list2)
    videos_list.update(videos_list3)
    return videos_list

# key 입력 받아서 영상 가져오는 함수
def get_key_data(key:str) -> dict:
    data = db.child('video').child(key).get()
    video_list=data.val()
    return video_list

# 카테고리 모아보기 정확한 입력 필요 최근 업로드 순
def get_category_data(category:str) -> dict:
    videos_list=Recently_category_group(category)
    return videos_list

# 채널 모아보기 정확한 입력 필요 최근 업로드 순
def get_channel_data(channel:str) -> dict:
    videos_list=Recently_channel_group(channel)
    return videos_list

# 검색 분류, 검색어 입력 필요
# 검색 분류에는 (제목:title, 채널: channel_name) 중 택 1
def get_search_title(pattern:str):
    videos_list=search_title(pattern)
    return videos_list

def get_search_channel_name(pattern:str):
    videos_list=search_channel_name(pattern)
    return videos_list

if __name__ == '__main__':
    print(get_index_data())
