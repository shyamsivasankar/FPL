import httpx

async def fixtures():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/fixtures/")
        return response.json()
    
async def userteam(managerid,gameweek):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/entry/"+managerid+"/event/"+gameweek+"/picks/")
        return response.json()

async def player(playerid):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/element-summary/"+str(playerid)+"/")
        return response.json()

async def overall():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/bootstrap-static/")
        return response.json()
    
async def managerHistory(managerid):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/entry/"+str(managerid)+"/history/")
        return response.json()

async def managerdata(managerid):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/entry/"+str(managerid)+"/")
        return response.json()

async def gameweek(n):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/event/"+n+"/live/")
        return response.json()