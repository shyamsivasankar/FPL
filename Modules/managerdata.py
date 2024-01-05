import httpx

async def managerdata(managerid):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/entry/"+str(managerid)+"/")
        return response.json()