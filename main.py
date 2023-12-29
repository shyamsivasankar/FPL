from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import json

app = FastAPI()
templates = Jinja2Templates(directory="templates")
session = requests.session()

@app.get('/',response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('Login.html',{'request':request})

@app.post('/Login')
async def login(req : Request, Username : str = Form() ,Password : str = Form()):
    url = 'https://users.premierleague.com/accounts/login/'
    payload = {
        'password' : Password,
        'login' : Username,
        'redirect_uri': 'https://fantasy.premierleague.com/a/login',
        'app': 'plfpl-web'
    }
    session.post(url, data=payload)
    response = session.get('https://fantasy.premierleague.com/drf/my-team/2730144')
    team_data = response.content

    return HTMLResponse(content=team_data, status_code=200)