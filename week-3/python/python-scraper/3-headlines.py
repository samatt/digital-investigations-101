import requests
from bs4 import BeautifulSoup

url = "https://www.stationindex.com/tv/markets/New+York"

response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.content

soup = BeautifulSoup(html, "html.parser")

table_div = soup.find("table")

table_rows = table_div.find_all("tr")

for row in table_rows:
    link = row.select("p.small a")
    # print(row.select("p.small a")[0]["href"])
