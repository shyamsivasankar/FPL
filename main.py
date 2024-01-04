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
                player_name.append([j['team_code'],j['web_name'],j['element_type']])
                break
    
    weekly_squad = []
    for i in player_name:
        for j in overall_data['teams']:
            if i[0] == j['code']:
                weekly_squad.append([i[1],j['name'],i[2]])
                break
    
    GK = []
    DEF = []
    MID = []
    STR = []
    SUB = weekly_squad[len(weekly_squad)-4:]
    weekly_squad= weekly_squad[:len(weekly_squad)-4]
    print(SUB)
    for i in weekly_squad:
        if i[2] == 1:
            GK.append(i)
        elif i[2] == 2:
            DEF.append(i)
        elif i[2] == 3:
            MID.append(i)
        else:
            STR.append(i)
    return templates.TemplateResponse('Team.html',{'request':req, 'GK':GK, 'DEF':DEF, 'MID':MID, 'STR':STR, 'SUB':SUB})

@app.get('/Team')
async def team(request: Request):
    return templates.TemplateResponse('Team.html',{'request':request})