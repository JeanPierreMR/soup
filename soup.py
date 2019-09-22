#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json, urllib, os
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
    #------printing title
    print(soup.title)
    print(soup.title.string)
    def get_links(content, soup):
        links = []
        for tag in soup.find_all('a', href=True):
            links.append(tag['href'])
        return links
    print(get_links(html_content,soup))
    #------printing Addres of UFM
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
    #------printing phone number
    for div in soup.find_all('div', class_="span4"):
        if (div.a != None ):
            if("Teléfono:" in div.text):
                print("----------")
                print(div.a.text)
                print("----------")
                break

    #------button ufmail
    result1 = soup.find_all('a', id="ufmail_")
    print(result1[0]['href'])
    #------button miu
    result1 = soup.find_all('a', id="miu_")
    print(result1[0]['href'])
    #-----images with href
    imgs = soup.find_all('img')
    for image in imgs:
        try:
            if(image["href"]!= None):
                print(image)
        except:
            pass
        
    #------counts all <a>
    result1 = soup.find_all('a')
    print(len(result1))
    #------creating csv with text and href from <a>
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
    #------changing page
    for div in soup.find_all('div', class_="menu-key"):
        print(div)
        print(div.a.text)
        try:
            print(div.a.text)
            if(div.a.text == "Estudios"):
                url=url_base+div.a['href'] 
                break
        except AssertionError as error:
            print(error)
   # Make a GET request to fetch the raw HTML content
    try:
        request_content = requests.get(url)
    except:
        print(f"unable to get {url}")
        sys.exit(1)
    html_content = request_content.text
    # Parse the html content, this is the Magic ;)
    soup = BeautifulSoup(html_content, "html.parser") 
    #------ Printing items of topmenu
    top_menu = soup.find_all('div', id="topmenu")
    print("-------------------")
    print(top_menu)
    #------ Printing all "Estudios"
    top_menu = soup.find_all('div', class_="estudios")
    for estudio in top_menu:
        print(estudio.text)
    #------ Printing all items from leftbar
    top_menu = soup.find_all('div', class_="leftbar")
    for item in top_menu:
        print(item.ul.text)
    #------ Printing social medias
    top_menu = soup.find_all('div', class_="social pull-right")
    for item in top_menu:
        for a in item.find_all('a'):
            print(a['href'])
    #------ Printing count of <a>
    result1 = soup.find_all('a')
    print(len(result1))

#executes instructions for estudios page
def Cs_ins():
    url="https://fce.ufm.edu/carrera/cs/"
    # Make a GET request to fetch the raw HTML content
    try:
        request_content = requests.get(url)
    except:
        print(f"unable to get {url}")
        sys.exit(1)
    html_content = request_content.text
    # Parse the html content, this is the Magic ;)
    soup = BeautifulSoup(html_content, "html.parser")
    #------ Printing title
    print(soup.title.string)
    #------ Downloading image of ufm
    img = soup.find_all('img', class_="fl-photo-img wp-image-500 size-full")
    urllib.request.urlretrieve(img[0]['src'], "ufm_logo.jpg")
    print(os.path.isfile("ufm_logo.jpg")) 
    #------ Printing meta title, description ("og")
    
    #------ Printing count of <a>
    result1 = soup.find_all('a')
    print(len(result1))
    #------ Printing count of <div>
    result1 = soup.find_all('div')
    print(len(result1))