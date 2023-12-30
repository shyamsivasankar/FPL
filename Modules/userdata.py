import httpx

async def userteam(managerid,gameweek):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/entry/"+managerid+"/event/"+gameweek+"/picks/")
        return response.json()