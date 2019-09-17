#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json
url_base = "http://ufm.edu"

#executes instructions for Portal page
def portal_ins():
    url=url_base+"/Portal"
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
        if (div.a != None ):
            try:
                if(div.a["href"] == "#myModal" or div.a["data-toggle"] == "modal"):
                    print(div.a.text)
                    break
            except:
                pass

    for div in soup.find_all('div', class_="span4"):
        if (div.a != None ):
            if("Teléfono:" in div.text):
                print("----------")
                print(div.a.text)
                print("----------")
                break


    # a = (soup.find_all('table', id="menu-table"))
    # print(a)
    #button ufmail
    result1 = soup.find_all('a', id="ufmail_")
    print(result1[0]['href'])
    #button miu
    result1 = soup.find_all('a', id="miu_")
    print(result1[0]['href'])
    #images with href
    imgs = soup.find_all('img')
    for image in imgs:
        try:
            if(image["href"]!= None):
                print(image)
        except:
            pass
        

    result1 = soup.find_all('a')
    print(len(result1))

    a_texts = []
    a_links = []
    for a in result1:
        if(a.text == ""):
            a_texts.append("No text")
        else:
            a_texts.append(a.text)
        a_links.append(a['href'])


    columnTitleRow = "text, link\n"
    with open('logs\extra_as.csv', 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(columnTitleRow)
        writer.writerows(zip(a_texts, a_links))
    with open('logs\extra_as.csv') as f:
        csv_f = csv.reader(f)
        for row in csv_f:
            print("-"*30)
            print('{:^20} || {}'.format(*row))
        print("-"*30)

#executes instructions for estudios page
def Estudios_ins():
    #changing page
    for div in soup.find_all('div', class_="menu-key"):
        print(div)
        # try:
        #     if(div.a.text == "Estudios"):
        #         url=url_base+a['href']
        # except:
        #     pass
        
    # Make a GET request to fetch the raw HTML content
    try:
        request_content = requests.get(url)
    except:
        print(f"unable to get {url}")
        sys.exit(1)
    html_content = request_content.text
    # Parse the html content, this is the Magic ;)
    soup = BeautifulSoup(html_content, "html.parser")
    print(html_content[:40])
    

