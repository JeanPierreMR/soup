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
    print(soup.title.string)
    
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
                print(div.a.findNext('a').text)
                print("----------")
                break
    #------ Printing nav menu
    result1 = soup.find_all('table', id="menu-table")[0].tr
    print("Menu-table items: ")
    result1.find_all('div')
    print(result1.find_all('div'))
    #------button ufmail
    result1 = soup.find_all('a', id="ufmail_")
    print("boton ufmail: "+ str(result1[0]['href']))
    #------button miu
    result1 = soup.find_all('a', id="miu_")
    print("boton miu: "+str(result1[0]['href']))
    #------Getting all properties that have href
    def get_links(content, soup):
        links = []
        for tag in soup.find_all('a', href=True):
            links.append(tag['href'])
        return links
    print(get_links(html_content,soup))
    #-----images with href
    imgs = soup.find_all('img')
    print(imgs)
    for image in imgs:
        try:
            if(image["href"]!= None):
                print(image)
        except:
            pass
        
    #------counts all <a>
    result1 = soup.find_all('a')
    print("Cantidad de <a>"+str(len(result1)))
    #------creating csv with text and href from <a>
    a_texts = ["text"]
    a_links = ["link"]
    for a in result1:
        if(a.text == ""):
            a_texts.append("No text")
        else:
            a_texts.append(a.text)
        a_links.append(a['href'])
    with open('logs\extra_as.csv', 'w+') as f:
        writer = csv.writer(f)
        writer.writerows(zip(a_texts, a_links))
    with open('logs\extra_as.csv') as f:
        csv_f = csv.reader(f)
        #print(f.readlines())
        for row in csv_f:
            print("-"*50)
            print(('{:^20} || {}'.format(*row)).replace("\n", ""))
        print("-"*50)

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
        try:
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
    print("------Top menu")
    print(top_menu)
    #------ Printing all "Estudios"
    print("------Estudios")
    top_menu = soup.find_all('div', class_="estudios")
    for estudio in top_menu:
        print(estudio.text)
    #------ Printing all items from leftbar
    print("------Left bar")
    top_menu = soup.find_all('div', class_="leftbar")
    for item in top_menu:
        print(item.ul.text)
    #------ Printing social medias
    print("------Social media")
    top_menu = soup.find_all('div', class_="social pull-right")
    for item in top_menu:
        for a in item.find_all('a'):
            #too slow to make each request for the title
            name = a['href'].split(".")[1].split("\\")[0]
            print(name, end='')
            print("\t" + str(a['href']))
    #------ Printing count of <a>
    result1 = soup.find_all('a')
    print("Cantidad de <a>"+str(len(result1)))

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
    meta = soup.find_all('meta', property = "og:title")
    print(meta[0])
    meta = soup.find_all('meta', property = "og:description")
    print(meta[0])
    #------ Printing count of <a>
    result1 = soup.find_all('a')
    print("Cantidad de <a>"+str(len(result1)))
    #------ Printing count of <div>
    result1 = soup.find_all('div')
    print("Cantidad de <div>"+str(len(result1)))
def directorio_ins():
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
    #table class = "tabla ancho100"   
    result1 = soup.find_all('table', class_= "tabla ancho100")
    for tabla in result1:
        a = tabla.find_all('a', href = True)
        print(a.sort())

portal_ins()
Estudios_ins()
Cs_ins()
