from fastapi import APIRouter

router = APIRouter()

@router.get("/user")
def user_get():
    return {
        "records": [
            {
                "name:": "Adam",
                "score": 100
                },
            {
                "name:": "Ban",
                "score": 200
            }
        ]
    }
