import random
from typing import Optional

from fastapi import FastAPI, Query

from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>my homepage</title>
        </head>
        <body>
            <h1>hello!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/")
async def root():
    html_content = """
    <html>
        <head>
            <title>Button Navigation Example</title>
        </head>
        <body>
            <h1>Welcome</h1>
            <button onclick="location.href='/index'">Go to Index page</button>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.post("/present")
async def give_present(present: str = Query(...)):
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しは{presentSelecter()}です。"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


def presentSelecter():
    present = ["キャンディー", "チョコレート", "ケーキ"]
    index = random.randint(0, len(present) - 1)
    return present[index]