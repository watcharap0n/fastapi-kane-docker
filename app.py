from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import line
from dependencies import get_token_header

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

app.include_router(
    line.router,
    prefix='/line',
    tags=['LINE'],
    dependencies=[Depends(get_token_header)],
    responses={400: {'message': 'error'}}
)


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})
