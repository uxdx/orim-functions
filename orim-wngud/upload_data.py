from datetime import datetime, timedelta
import datetime
import pyrebase
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# secrets.json 로딩
with open("secrets.json") as jsonFile:
    secrets = json.load(jsonFile)
    jsonFile.close()
config = secrets['config']
# 파이어베이스 인스턴스 생성
firebase = pyrebase.initialize_app(config)
# 데이터베이스 인스턴스 생성
db = firebase.database()

def upload_video(title:str,uploadDate:datetime.datetime,url:str,thumbnail:str, like:int,view:int, category:str):
    db.child('videos').push({
        'title':title,
        'uploadDate': uploadDate.__str__(),
        'url':url,
        'thumbnail': thumbnail,
        'like': like,
        'view': view,
        'category': category
    })

def upload_video_from_dict(dic:dict):
    upload_video(dic['title'], dic['uploadDate'], dic['url'], dic['thumbnail'], dic['like'], dic['view'], dic['category'])

sample_video = {
    "title": '【12/30】 도파 in 실버 지옥에서온 탑 피오라 vs 루시안 ( Piora vs Lucian Dopa In silver Dec.30 )',
    'uploadDate': datetime.datetime(2020,1,3),
    'url': 'https://www.youtube.com/watch?v=puQ-MzqB9jw',
    'thumbnail': 'https://i.ytimg.com/an_webp/puQ-MzqB9jw/mqdefault_6s.webp?du=3000&sqp=CKSQpI8G&rs=AOn4CLDQ7gNlVqGVjWuo-LwONQCuxEh3FQ',
    'like': 123456,
    'view': 654321,
    'category': 'game'
}

if __name__ == '__main__':
    # upload_video_from_dict(sample_video)
    pass