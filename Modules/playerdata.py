# https://fantasy.premierleague.com/api/element-summary/{player-id}/
import httpx

async def player(playerid):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://fantasy.premierleague.com/api/element-summary/"+str(playerid)+"/")
        return response.json()