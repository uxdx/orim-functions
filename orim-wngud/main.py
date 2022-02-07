from flask import Flask, render_template
from flask_assets import Environment, Bundle

from get_data import get_index_data

import os

# 플라스크 앱 인스턴스 생성
app = Flask(__name__)

# SCSS 세팅
assets = Environment(app)
assets.url = app.static_url_path # =static/
scss = Bundle('scss/index.scss', filters='pyscss', output='all.css') # all.css 로 컴파일되서 assets.url(static/)에 저장됨
assets.register('scss_all', scss)

@app.route('/', methods=['POST', 'GET'])
def index():
    service = os.environ.get('K_SERVICE', 'Unknown service')
    revision = os.environ.get('K_REVISION', 'Unknown revision')
    firebase_config = os.environ.get('FIREBASE_CONFIG')
    print(firebase_config)
    
    return render_template('index.html',
        video_list=get_index_data(),
        config=firebase_config,
        Service=service,
        Revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')