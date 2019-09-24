#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json, urllib, os
url_base = "http://ufm.edu"



#executes instructions for Portal page
def portal_ins():
    text = ""
    url=url_base+"/Portal"
    # Make a GET request to fetch the raw HTML content
    try:
        request_content = requests.get(url)
    except:
        text = text + str(f"unable to get {url}")
        sys.exit(1)
    html_content = request_content.text
    # Parse the html content, this is the Magic ;)
    soup = BeautifulSoup(html_content, "html.parser")
    #------printing title
    text = text + "\n"+str(soup.title.string)
    
    #------printing Addres of UFM
    #searches for div and then gets <a> by its href
    a = (soup.find_all('div', class_="span4"))
    for div in soup.find_all('div', class_="span4"):
        if (div.a != None ):
            try:
                if(div.a["href"] == "#myModal" or div.a["data-toggle"] == "modal"):
                    text = text + "\n"+str(div.a.text)
                    break
            except:
                pass
    #------printing phone number
    for div in soup.find_all('div', class_="span4"):
        if (div.a != None ):
            if("Teléfono:" in div.text):
                text = text + "\n"+str("----------")
                text = text + "\n"+str(div.a.text)
                text = text + "\n"+str(div.a.findNext('a').text)
                text = text + "\n"+str("----------")
                break
    #------ Printing nav menu
    result1 = soup.find_all('table', id="menu-table")[0].tr
    text = text + "\n"+str("Menu-table items: ")
    result1.find_all('div')
    text = text + "\n"+str(result1.find_all('div'))
    #------button ufmail
    result1 = soup.find_all('a', id="ufmail_")
    text = text + "\n"+str("boton ufmail: "+ str(result1[0]['href']))
    #------button miu
    result1 = soup.find_all('a', id="miu_")
    text = text + "\n"+str("boton miu: "+str(result1[0]['href']))
    #------Getting all properties that have href
    def get_links(content, soup):
        links = []
        for tag in soup.find_all('a', href=True):
            links.append(tag['href'])
        return links
    text = text + "\n"+str(get_links(html_content,soup))
    #-----images with href
    imgs = soup.find_all('img')
    text = text + "\n"+str(imgs)
    for image in imgs:
        try:
            if(image["href"]!= None):
                text = text + "\n"+str(image)
        except:
            pass
        
    #------counts all <a>
    result1 = soup.find_all('a')
    text = text + "\n"+str("Cantidad de <a>"+str(len(result1)))
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
        #text = text + "\n"+str(f.readlines())cv
        for row in csv_f:
            text = text + "\n"+str("-"*50)
            text = text + "\n"+str(('{:^20} || {}'.format(*row)).replace("\n", ""))
        text = text + "\n"+str("-"*50)
    return text
#executes instructions for estudios page
def Estudios_ins():
    text = ""
    url=url_base+"/Portal"
    # Make a GET request to fetch the raw HTML content
    try:
        request_content = requests.get(url)
    except:
        text = text + "\n"+str(f"unable to get {url}")
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
            text = text + "\n"+str(error)
   # Make a GET request to fetch the raw HTML content
    try:
        request_content = requests.get(url)
    except:
        text = text + "\n"+str(f"unable to get {url}")
        sys.exit(1)
    html_content = request_content.text
    # Parse the html content, this is the Magic ;)
    soup = BeautifulSoup(html_content, "html.parser") 
    #------ Printing items of topmenu
    top_menu = soup.find_all('div', id="topmenu")
    text = text + "\n"+str("------Top menu")
    text = text + "\n"+str(top_menu)
    #------ Printing all "Estudios"
    text = text + "\n"+str("------Estudios")
    top_menu = soup.find_all('div', class_="estudios")
    for estudio in top_menu:
        text = text + "\n"+str(estudio.text)
    #------ Printing all items from leftbar
    text = text + "\n"+str("------Left bar")
    top_menu = soup.find_all('div', class_="leftbar")
    for item in top_menu:
        text = text + "\n"+str(item.ul.text)
    #------ Printing social medias
    text = text + "\n"+str("------Social media")
    top_menu = soup.find_all('div', class_="social pull-right")
    for item in top_menu:
        for a in item.find_all('a'):
            #too slow to make each request for the title
            name = a['href'].split(".")[1].split("\\")[0]
            text = text + "\n"+str(name)
            text = text +str("\t" + str(a['href']))
    #------ Printing count of <a>
    result1 = soup.find_all('a')
    text = text + "\n\n"+str("Cantidad de <a>"+str(len(result1)))
    return text
#executes instructions for computer science page
def Cs_ins():
    text = ""
    url="https://fce.ufm.edu/carrera/cs/"
    # Make a GET request to fetch the raw HTML content
    try:
        request_content = requests.get(url)
    except:
        text = text + "\n"+str(f"unable to get {url}")
        sys.exit(1)
    html_content = request_content.text
    # Parse the html content, this is the Magic ;)
    soup = BeautifulSoup(html_content, "html.parser")
    #------ Printing title
    text = text + "\nTitulo: "+str(soup.title.string)
    #------ Downloading image of ufm
    img = soup.find_all('img', class_="fl-photo-img wp-image-500 size-full")
    urllib.request.urlretrieve(img[0]['src'], "ufm_logo.jpg")
    #------ Printing meta title, description ("og")
    meta = soup.find_all('meta', property = "og:title")
    text = text + "\n"+str(meta[0]['content'])
    meta = soup.find_all('meta', property = "og:description")
    text = text + "\n"+str(meta[0]['content'])
    #------ Printing count of <a>
    result1 = soup.find_all('a')
    text = text + "\n\n"+str("Cantidad de <a>"+str(len(result1)))
    #------ Printing count of <div>
    result1 = soup.find_all('div')
    text = text + "\n\n"+str("Cantidad de <div>"+str(len(result1)))
    return text
#executes instructions for directory
def directorio_ins():
    text = ""
    url="https://www.ufm.edu/Directorio"
    # Make a GET request to fetch the raw HTML content
    try:
        request_content = requests.get(url)
    except:
        text = text + "\n"+str(f"unable to get {url}")
        sys.exit(1)
    html_content = request_content.text
    # Parse the html content, this is the Magic ;)
    soup = BeautifulSoup(html_content, "html.parser")
    #------Geting emails
    result1 = soup.find_all('table')
    emails = []
    for tabla in result1:
        a_s = tabla.find_all('a', href = True)
        for a in a_s:
            if("@" in a.text):
                emails.append(a['href'].replace("mailto:",""))
    with open('logs\\4directorio_emails.txt', 'w+') as f:
        f.write(str(sorted(emails)))
    #------Counting emails that start with a vowel
    count = 0
    for email in emails:
        if (email.startswith(('a', 'e', 'i', 'o', 'u'))):
            count +=1
    text = text + "\n"+str(f"\nemails starting with vowel: {count}" )
    #------Getting rows with same address
    result1 = soup.find_all('table', class_= "tabla ancho100")
    directorio = {}
    for table in result1:
        for tr in table.find_all('tr'):
            name = ""
            direction = ""
            try:
                name=(tr.td.a.text).replace(" ", "").replace("\n", "")
                direction = (tr.find_all('td')[4].text.split(",")[0]).strip()
            except:
                try:
                    name=(tr.td.text).replace(" ", "").replace("\n", "")
                    direction = (tr.find_all('td')[4].text.split(",")[0]).strip()
                except:
                    try:
                        name=(tr.td).replace(" ", "").replace("\\n", "")
                        direction = (tr.find_all('td')[4].text.split(",")[0]).strip()
                    except:
                        next
            if(name != ''):
                try:
                    directorio.get(direction).append(name)
                except:
                    directorio.update({direction: [name]})
    with open('logs\\4directorio_address.json', 'w+') as f:
        f.write(str(directorio))
    #------gettting phones
    # directorio_telefono = {}
    # for table in result1:
    #     for tr in table.find_all('tr'):
    #         name = ""
    #         telefono = ""
    #         try:
    #             name=(tr.td.a.text).replace(" ", "").replace("\n", "")
    #             telefono = (tr.find_all('td')[2]).text
    #         except:
    #             try:
    #                 name=(tr.td.text).replace(" ", "").replace("\n", "")
    #                 telefono = (tr.find_all('td')[2]).text
    #             except:
    #                 try:
    #                     name=(tr.td).replace(" ", "").replace("\\n", "")
    #                     telefono = (tr.find_all('td')[2]).text
    #                 except:
    #                     next
    #         if(name != ''):
    #             try:
    #                 directorio_telefono.get(name).append(telefono)
    #             except:
    #                 directorio_telefono.update({name: [telefono]})
    # text = text + "\n"+str(directorio_telefono)
    # result1 = soup.find_all('table', class_="tabla ancho100 col3")
    # for table in result1:
    #     if ("Decanos y Directores" in table.th.text):
    #         text = text + "\n"+str(table)
    #         trs = table.find_all('tr')
    #         for tr in trs:
    #             text = text + "\n"+str(tr)
    #         break
    # return text

def check_size(text):
    if(text.count("\n")>30):
        print("Output exceeds 30 lines, sending output to: <logfile>")
        with open('logs\\logfile.txt', 'w+') as f:
            f.write(text)
    else:
        print(text)


def main():
    desition = sys.argv[0]
    if(desition == '1'):
        check_size(portal_ins())
    elif(desition == '2'):
        check_size(Estudios_ins())
    elif(desition == '3'):
        check_size(Cs_ins())
    elif(desition == '4'):
        check_size(directorio_ins())
    elif(desition == '5'):
        full = ""
        full = full + "\n" + str(portal_ins())
        full = full + "\n" + str(Estudios_ins())
        full = full + "\n" + str(Cs_ins())
        full = full + "\n" + str(directorio_ins())
        check_size(full)

main()

