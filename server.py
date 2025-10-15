from fastapi import FastAPI, Request
from modules.browse import browse_url
import uvicorn

app = FastAPI()

@app.post("/command/browse")
async def browse_command(request: Request):
    """
    Expects JSON: {"url": "...", "keyword": "..."} (keyword optional)
    Returns HTML and/or keyword search results.
    """
    data = await request.json()
    url = data.get("url")
    keyword = data.get("keyword")
    if not url:
        return {"error": "Missing 'url' parameter"}
    result = browse_url(url, keyword)
    return result

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000)