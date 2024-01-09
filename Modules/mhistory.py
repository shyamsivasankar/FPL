import httpx

async def managerHistory(managerid):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/entry/"+str(managerid)+"/history/")
        return response.json()