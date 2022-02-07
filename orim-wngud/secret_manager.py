import json
import os

from google.cloud import secretmanager

def access_secret(project_id = "jinho-337705" , secret_id = "Firebase" , version_id = 1) -> str:
    # 아래 부분에서 에러가 안나려면 GCP에서 '서비스계정' 에서 계정을 만들고,
    # '키' 부분에서 키를 하나 만든다음 그 키(json파일)를 다운로드해서
    # 환경변수 $env:GOOGLE_APPLICATION_CREDENTIALS="C:주소.json"
    # 등록을 하면 그 컴퓨터는 아래 함수를 사용 가능
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})

    payload = response.payload.data.decode("UTF-8")
    return json.loads(payload)

def access_secret_as_env(env:str):
    return os.environ.get(env)

def access_secret_as_file():
    pass
if __name__ == '__main__':
    print(access_secret())
    pass