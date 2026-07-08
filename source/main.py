# Webサーバーを起動
# 作成: kanato-shimabukuro

from fastapi import FastAPI
import uvicorn
from router import router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv() # envファイルから環境変数を読み込む

api = FastAPI()

api.include_router(router)

api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'], # CORS設定 | 全てのオリジンからのアクセスを許可
    allow_methods=['*'],
    allow_headers=['*']
)

if __name__ == '__main__':
    uvicorn.run('main:api', host='0.0.0.0', port=8000, reload=True)