from fastapi import HTTPException, Header


async def get_token_header(X_Line_Token: str = Header(...)):
    if X_Line_Token != 'Mango-Token':
        raise HTTPException(status_code=400, detail='X-Token Header invalid')
