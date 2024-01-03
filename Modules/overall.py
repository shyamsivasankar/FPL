import httpx

async def overall():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/bootstrap-static/")
        return response.json()