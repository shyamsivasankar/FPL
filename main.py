from fastapi import FastAPI,Request,Form, HTTPException, Response, Cookie, Depends
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

from Modules.userdata import userteam
from Modules.playerdata import player
from Modules.overall import overall
from Modules.gameweek import gameweek
from Modules.managerdata import managerdata
from Modules.mhistory import managerHistory
from Modules.fixtures import fixtures
from Modules.Team_data import team_data

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory='static'),name='static')

@app.get('/',response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('Login.html',{'request':request})

@app.get('/overall_data_fetch')
async def Overall_data_fetch(request: Request):
    data = await overall()
    return data

@app.get('/fixtures')
async def fixtures_data(request: Request):
    data = await fixtures()
    return data

@app.post('/Login')
async def login(req : Request, response: Response, managerid : str = Form()):
    response.set_cookie(key="managerid",value=managerid)
    data = await team_data(managerid=managerid)
    data['request'] = req
    return templates.TemplateResponse('Team.html', data)

@app.get('/Team')
async def team(request: Request):
    return templates.TemplateResponse('Team.html',{'request':request})

@app.post('/navbar')
async def compare_teams(request: Request, managerid: str = Depends(Cookie("managerid"))):
    return {"data" : managerid}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)