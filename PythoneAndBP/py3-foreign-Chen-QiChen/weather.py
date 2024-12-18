import aiohttp
import asyncio
import sys
from install import install

try:
    import pandas as pd
except ImportError:
    print("缺少pandas库，正在安装...")
    install("pandas")
    import pandas as pd


try:
    from tabulate import tabulate
except ImportError:
    print("缺少tabulate库，正在安装...")
    install("tabulate")
    from tabulate import tabulate

commonurl = "https://api.open-meteo.com/v1/forecast"


async def fetch_data(session, url, params=None):
    async with session.get(url, params=params) as response:
        if response.status == 200:
            data = await response.json()
            return data
        else:
            print(f"http erro: {response.status}")
            return None


async def get_temperature(session, country, city, latitude, longitude, results):
    params = {"latitude": latitude, "longitude": longitude, "current_weather": "true"}
    data = await fetch_data(session, commonurl, params=params)
    if data:
        temperature = data["current_weather"]["temperature"]
        results.append([city, country, f"{temperature}°C"])


async def main(file_path):
    # 使用pandas读取CSV文件
    df = pd.read_csv(file_path)

    # 创建异步HTTP客户端会话
    async with aiohttp.ClientSession() as session:
        tasks = []
        results = []
        for _, row in df.iterrows():
            country = row["country"]
            capital = row["capital"]
            latitude = row["latitude"]
            longitude = row["longitude"]
            task = asyncio.create_task(
                get_temperature(session, country, capital, latitude, longitude, results)
            )
            tasks.append(task)

        # 并发执行所有任务
        await asyncio.gather(*tasks)

        # 打印结果表格
        print(
            tabulate(
                results, headers=["City", "Country", "Temperature"], tablefmt="grid"
            )
        )


if __name__ == "__main__":
    file_path = sys.argv[1]  # 从命令行获取文件路径
    asyncio.run(main(file_path))
