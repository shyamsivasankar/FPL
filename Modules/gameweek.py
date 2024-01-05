import httpx

async def gameweek(n):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/event/"+n+"/live/")
        return response.json()