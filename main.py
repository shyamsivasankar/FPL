from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from Modules.userdata import userteam
from Modules.playerdata import player
import jsons

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory='static'),name='static')

@app.get('/',response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('Login.html',{'request':request})

@app.post('/Login')
async def login(req : Request, managerid : str = Form()):
    data = await userteam(managerid=managerid,gameweek=str(19))
    p1 = await player(playerid=data['picks'][0]['element'])
    return p1

@app.get('/Team')
async def team(request: Request):
    return templates.TemplateResponse('Team.html',{'request':request})