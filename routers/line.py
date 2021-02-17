from fastapi import APIRouter, HTTPException, Body
from typing import Optional

router = APIRouter()


@router.post('/{userId}')
async def api_line_mango(userId: str, payload: Optional[dict] = Body(None)):
    """
    POST LINE-userId-Mango-Ken
    - **payload**: any
    :param payload:
    :param userId:
    :return:
    """
    try:
        return {'UserId': userId, 'Payload': payload}
    except Exception:
        raise HTTPException(status_code=400, detail='Methods POST and POST JSON')
