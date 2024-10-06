from fastapi import APIRouter

router = APIRouter()

records = {
        "records": [
            {
                "name": "Adam",
                "score": 100
                },
            {
                "name": "Ban",
                "score": 200
            }
        ]
    }

@router.get("/user")
def get_records():
    return records

@router.get("/user/{id}")
def get_record_by_id(id: int):
    record = records["records"][id]
    return record