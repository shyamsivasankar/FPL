from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

from Modules.userdata import userteam
from Modules.playerdata import player
from Modules.overall import overall
from Modules.gameweek import gameweek
from Modules.managerdata import managerdata
from Modules.mhistory import managerHistory
import jsons

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory='static'),name='static')

@app.get('/',response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('Login.html',{'request':request})

@app.post('/Login')
async def login(req : Request, managerid : str = Form()):
    manager_data = await managerdata(managerid=managerid)
    current_event = manager_data['current_event']
    user_data = await userteam(managerid=managerid,gameweek=str(current_event))
    overall_data =  await overall()
    week_details = await gameweek(str(current_event))
    mHist = await managerHistory(managerid=managerid)

    gw_points = [i['points'] for i in mHist['current']]
    x_axis = [str(i) for i in range(len(gw_points))]
    player_name =[]

    manager = { "first_name": manager_data['player_first_name'],
               "last_name" : manager_data['player_last_name'],
               "gw_points" : manager_data['summary_event_points'],
               "overall_points" : manager_data['summary_overall_points'],
               "gw_rank" : manager_data['summary_event_rank'],
               "overall_rank" : manager_data['summary_overall_rank'],
               "value" : float(user_data['entry_history']['value'])/10,
               "gw" : current_event}
    
    for i in user_data['picks']:
        for j in overall_data['elements']:
            if i['element'] == j['id']:
                player_name.append({'team_code' :j['team_code'],
                                    'web_name' : j['web_name'],
                                    'element_type' : j['element_type'],
                                    'id' : j['id'],
                                    'first_name' : j['first_name'],
                                    'second_name' : j['second_name'],
                                    'total_points' : j['total_points'],
                                    'minutes' : j['minutes'],
                                    'goals_scored' : j['goals_scored'],
                                    'assists' : j['assists'],
                                    'clean_sheets' : j['clean_sheets'],
                                    'expected_goals' : j['expected_goals'],
                                    'expected_assists' : j['expected_assists'],
                                    'expected_goal_involvements' : j['expected_goal_involvements'],
                                    'transfers_in_event' : j['transfers_in_event'],
                                    'transfers_out_event' : j['transfers_out_event'],
                                    'is_captain' : i['is_captain']})
                break

    avg_pts = []
    hst_pts = []
    for i in overall_data['events']:
        avg_pts.append(i['average_entry_score'])
        hst_pts.append(i['highest_score'])

    for i in avg_pts:
        if i==0:
            avg_pts.remove(i)
    
    for i in hst_pts:
        if i==None:
            hst_pts.remove(i)
    avg_pts = avg_pts[:current_event]
    hst_pts = hst_pts[:current_event]


    for i in player_name:
        for j in week_details['elements']:
            if i['id']==j['id']:
                i['points'] = (j['stats']['total_points'])
                break
        

    for i in player_name:
        for j in overall_data['teams']:
            if i['team_code'] == j['code']:
                i['team_name'] = j['name']
                break
    
    leagues = []
    for i in manager_data['leagues']['classic']:
        leagues.append([i['name'],i['entry_rank'],i['entry_last_rank']])
    
    GK = []
    DEF = []
    MID = []
    STR = []
    SUB = player_name[len(player_name)-4:]
    player_name= player_name[:len(player_name)-4]
    for i in player_name:
        if i['element_type'] == 1:
            GK.append(i)
        elif i['element_type']== 2:
            DEF.append(i)
        elif i['element_type'] == 3:
            MID.append(i)
        else:
            STR.append(i)
    
    fpl_team = [GK,DEF,MID,STR]

    return templates.TemplateResponse('Team.html',{'request':req, 
                                       'fpl_team':fpl_team, 
                                       'SUB':SUB, 
                                       'Manager': manager,
                                       'GWH': gw_points,
                                       'x':x_axis,
                                       'leagues':leagues,
                                       'avg_pts':avg_pts,
                                       'hst_pts':hst_pts})

@app.get('/Team')
async def team(request: Request):
    return templates.TemplateResponse('Team.html',{'request':request})

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')