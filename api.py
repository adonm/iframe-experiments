# api.py
# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "fastapi[standard]",
# ]
# ///

import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates("static")

@app.get("/hello")
def hello():
    return {"message": "Hello World"}

@app.get("/content.html")
def content(request: Request):
    appurl = request.url_for("static", path="index.html")
    appurl = appurl.replace(hostname=appurl.hostname.replace("portal-", "app-"))
    return templates.TemplateResponse(request=request, name="content.html", context={"appurl": appurl})

app.mount("/", StaticFiles(directory="static", html=True), name="static")


def main() -> None:
    uvicorn.run("api:app", reload=True)

if __name__ == "__main__":
    main()
