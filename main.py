from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

#1
@app.get("/1")
async def main():
    return HTMLResponse(
        content=open("1.html", "r", encoding="utf-8").read()
    )


@app.get("/Home.html")
async def root():
    return HTMLResponse(
        content=open("Home.html", "r", encoding="utf-8").read()
    )

#Refractive.html
@app.get("/Content/Refractive.html")
async def Refractive_html():
    return HTMLResponse(
        content=open("Content\Refractive.html", "r", encoding="utf-8").read()
    )

#相速度与群速度.html
@app.get("/Content/相速度与群速度.html")
async def 相速度与群速度_html():
    return HTMLResponse(
        content=open("Content\相速度与群速度.html", "r", encoding="utf-8").read()
    )


#Bessel.html
@app.get("/Bessel.html")
async def Bessel_html():
    return HTMLResponse(
        content=open("Bessel.html", "r", encoding="utf-8").read()
    )



#HTMLs/2024.5.1.html
@app.get("/2024_5_1.html")
async def Bessel_html():
    return HTMLResponse(
        content=open(r"HTMLs\2024_5_1.html", "r", encoding="utf-8").read()
    )