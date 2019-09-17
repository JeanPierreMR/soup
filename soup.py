#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    request_content = requests.get(url)
except:
    print(f"unable to get {url}")
    sys.exit(1)
html_content = request_content.text
# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())

print(soup.title)
print(soup.title.string)
input()
# for div in soup.find_all("div"):
#     print(div)
#     print("--------------------------")
def get_links(content, soup):
    links = []
    for tag in soup.find_all('a', href=True):
        links.append(tag['href'])
    return links


print(get_links(html_content,soup))


# file = open("result.txt", 'w+') 
# file.write('ress')
# print(file.read())

#searches for div and then gets <a> by its href
a = (soup.find_all('div', class_="span4"))
for div in soup.find_all('div', class_="span4"):
    if (div.a != None and div.a["href"] == "#myModal"):
        print(div.a.text)
        break


