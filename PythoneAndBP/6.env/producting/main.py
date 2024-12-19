from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
import pandas as pd
import aiohttp
import asyncio

# 代理服务器的配置
PROXY_HOST = "localhost"
PROXY_PORT = 8000
FetchURL = "https://api.open-meteo.com/v1/forecast"
app = FastAPI()
app.mount("/static", StaticFiles(directory="../vue_project/dist"), name="static")
templates = Jinja2Templates(directory="../vue_project/dist")
df = pd.read_csv("europe.csv")

# 定义全局变量
results = []


async def fetch_data(session, url, params=None):
    async with session.get(url, params=params) as response:
        if response.status == 200:
            data = await response.json()
            return data
        else:
            print(f"http error: {response.status}")
            return None


async def get_temperature(session, country, city, latitude, longitude):
    params = {"latitude": latitude, "longitude": longitude, "current_weather": "true"}
    data = await fetch_data(session, FetchURL, params=params)
    if data:
        temperature = data["current_weather"]["temperature"]
        return {"city": city, "country": country, "temperature": f"{temperature}°C"}
    return None


async def update():
    global results  # 声明使用全局变量
    async with aiohttp.ClientSession() as session:
        tasks = []
        results = []  # 清空全局结果
        for _, row in df.iterrows():
            country = row["country"]
            capital = row["capital"]
            latitude = row["latitude"]
            longitude = row["longitude"]
            task = get_temperature(session, country, capital, latitude, longitude)
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        results = [result for result in results if result is not None]  # 过滤 None 值


@app.get("/")
async def home(request: Request):
    await update()  # 更新全局 results
    context = {"request": request, "message": "服务器已连接", "data": results}
    print("Server connected")
    return templates.TemplateResponse("index.html", context)


@app.get("/F5")
async def F5(request: Request):
    await update()  # 更新全局 results
    context = {"request": str(request.url), "message": "数据已更新", "data": results}
    print("Data has been updated")
    return JSONResponse(content=context)


@app.post("/add")
async def add(request: Request):
    body = await request.json()
    print(body)
    capital = body.get("capital")
    country = body.get("country")
    longitude = body.get("longitude")
    latitude = body.get("latitude")

    async with aiohttp.ClientSession() as session:
        result = await get_temperature(session, country, capital, latitude, longitude)

    if result:
        results.append(result)  # 将新结果添加到全局 results
    print("Data added")
    return JSONResponse(content={"message": "数据已处理", "data": result})


@app.delete("/delete")
async def delete(request: Request):
    body = await request.json()
    city = body.get("city")
    country = body.get("country")

    global results
    # 查找要删除的项
    for index, item in enumerate(results):
        if item["city"] == city and item["country"] == country:
            del results[index]  # 删除指定的项
            print("Data deleted")
            return JSONResponse(content={"message": "数据已删除", "result": item})

    # 如果没有找到要删除的项，返回404错误
    print("No data was found to delete")
    raise HTTPException(status_code=404, detail="未找到要删除的数据")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=PROXY_HOST, port=PROXY_PORT)
