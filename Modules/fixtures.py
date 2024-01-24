import httpx

async def fixtures():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/fixtures/")
        return response.json()