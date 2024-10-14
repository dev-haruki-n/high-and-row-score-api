from fastapi import FastAPI
from routers import user_api

from fastapi.middleware.cors import CORSMiddleware

allowed_origins = [
    # "https://example.com",       # 特定のドメインを許可
    # "https://sub.example.com",   # サブドメインを許可
    "http://localhost:3000",     # ローカル開発環境でNext.jsが動作している場合 これを恐らく環境変数で設定
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = allowed_origins,  # 必要に応じてクライアントのURLを指定
    allow_credentials = True,
    allow_methods = ["GET"],
    allow_headers = ["*"],
)

app.include_router(user_api.router)