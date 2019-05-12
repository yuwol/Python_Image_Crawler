import os
import shutil
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
from requests import get
from urllib.request import urlopen, Request

def search(dirname):
    try:      
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                print(full_filename)
                search(full_filename)
            else:
                print(full_filename + " - 이동 ")

    except PermissionError:
        pass
def search(dirname):
    try:      
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                print(full_filename)
                #search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                videos = ['.mp4','.avi','.mpg','.mpeg']
                if ext in videos: 
                    term = os.path.splitext(filename)[0]
#                    if(os.path.exists(os.path.join(os.getcwd(), term.upper() + '.jpg'))):
#                        print(term.upper() + ' - exists')
#                    else:
                    with requests.Session() as s:
                        first_page = s.get("https://www.arzon.jp/itemlist.html?t=&m=all&s=&q=" + term)
                        html = first_page.text
                        soup = bs(html, 'html.parser')
#                            print(html)
                        csrf = soup.find('td', {'class': 'yes'}) # input태그 중에서 name이 _csrf인 것을 찾습니다.
                        children = csrf.findChildren("a" , recursive=False)
                        redirection = ''
                        for child in children:
                            redirection = child['href']
                            print(child['href'])

                        post_one = s.get('https://www.arzon.jp' + redirection)
                        print(post_one)
                        soup = bs(post_one.text, 'html.parser') # Soup으로 만들어 줍시다.
                        contents = soup.select('dl.hentry dt a img')
                        print(contents) 
                        if len(contents) > 0:    
                            downloadURL = 'https:' + contents[0]['src'].replace('S','L')                                  
                            print(downloadURL)

                            s.headers.update({'referer': "https://www.arzon.jp"})
                            r = s.get(downloadURL)
                            print(r)
                            open(os.path.join(os.getcwd(), term + '.jpg'), 'wb').write(r.content)
    except PermissionError:
        pass
search(os.getcwd())