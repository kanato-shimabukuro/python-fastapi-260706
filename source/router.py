# ルーティング処理
# 作成: kanato-shimabukuro

from fastapi import APIRouter
from test import Test

router = APIRouter()

# ----------------------------------------------------------------------------------------------------

@router.get('/')
def route_1():
    return Test().version()