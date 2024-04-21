from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse(
        content=open("Home.html", "r", encoding="utf-8").read()
    )

#Refractive.html
@app.get("/Refractive.html")
async def Refractive_html():
    return HTMLResponse(
        content=open("Content/Refractive.html", "r", encoding="utf-8").read()
    )

#相速度与群速度.html
@app.get("/相速度与群速度.html")
async def 相速度与群速度_html():
    return HTMLResponse(
        content=open("Content/相速度与群速度.html", "r", encoding="utf-8").read()
    )