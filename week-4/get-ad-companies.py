from urllib import response
import requests
from bs4 import BeautifulSoup

url = "https://digitaladvertisingalliance.org/participating"

response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
#Get all the elements with views-field and views-field-nothing classes 
items = soup.findAll("div", attrs={"class": "views-field views-field-nothing"})

# Add header with the output file column names
lines = ["link, name\n"]

for item in items:

    # Get the link to the companies URL.
    link = item.select("a")[0]["href"]
    # Get the name of the company from the image alt-text.
    name = item.select("img")[0]["alt"]
    
    # add the url and company name to a string in the format link,company_name.
    new_line = link + "," + name + "\n" 

    # add that line to the list of lines.
    lines.append(new_line)



with open("ad-companies.csv","w") as outfile:
    # Use the writelines method to write the list of strings to a file.
    outfile.writelines(lines)