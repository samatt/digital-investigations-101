import requests

# pip install requests
# pip install beautifulsoup4

resp = requests.get("https://www.gutenberg.org/cache/epub/996/pg996.txt")
dq_text = resp.text
filename = "dq.txt"
with open(filename, "w") as outfile:
    outfile.write(dq_text)
