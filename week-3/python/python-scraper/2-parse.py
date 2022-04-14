import requests
from bs4 import BeautifulSoup

# url = "https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s"
url = "https://digitaladvertisingalliance.org/participating"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html = response.content

soup = BeautifulSoup(html, "html.parser")
items = soup.findAll("div", attrs={"class": "views-field views-field-nothing"})

# print(soup.prettify())
# print(items)
# info-box-content-item
lines = ["link, name\n"]
for item in items:
    link = item.select("a")[0]["href"][:-1]
    img = item.select("img")[0]["alt"]
    new_line = link + "," + img + "\n"
    lines.append(new_line)
    # print(f"{link}, {img}", link, img)
# for row in soup.findAll("a"):
#     print(row.prettify())

with open("ad-company-urls.csv", "w") as outfile:
    outfile.writelines(lines)


# component-newyork-latest-news-frontdoor > div:nth-child(2) > article:nth-child(3) > a:nth-child(1)
