from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from Modules.userdata import userteam
from Modules.playerdata import player
from Modules.overall import overall
import jsons

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory='static'),name='static')

@app.get('/',response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('Login.html',{'request':request})

@app.post('/Login')
async def login(req : Request, managerid : str = Form()):
    user_data = await userteam(managerid=managerid,gameweek=str(20))
    overall_data =  await overall()
    player_name =[]
    for i in user_data['picks']:
        for j in overall_data['elements']:
            if i['element'] == j['id']:
                player_name.append([j['first_name'],j['second_name'],j['web_name']])
                break
    return player_name
    # p1 = await player(playerid=data['picks'][0]['element'])
    # return data['picks']
    # return overall_data['elements'][0]

@app.get('/Team')
async def team(request: Request):
    return templates.TemplateResponse('Team.html',{'request':request})