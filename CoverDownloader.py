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
                #print(filename + ' ' + dirname)                
                #if filename != "새 폴더" and dirname != os.getcwd():
                #if filename != "새 폴더" :
                print(full_filename)
                search(full_filename)
            else:
                print(full_filename + " - 이동 ")
                term = os.path.splitext(filename)[0]
                print(term + " - 이동 ")
                s = requests.Session()

                with requests.Session() as s:
                    # 우선 클리앙 홈페이지에 들어가 봅시다.
                    first_page = s.get("https://www.arzon.jp/itemlist.html?t=&m=all&s=&q=" + term)
                    html = first_page.text
                    soup = bs(html, 'html.parser')
                    csrf = soup.find('td', {'class': 'yes'}) # input태그 중에서 name이 _csrf인 것을 찾습니다.
                    children = csrf.findChildren("a" , recursive=False)
                    redirection = ''
                    for child in children:
                        redirection = child['href']
                        print(child['href'])

                    post_one = s.get('https://www.arzon.jp' + redirection)
                    soup = bs(post_one.text, 'html.parser') # Soup으로 만들어 줍시다.
                    contents = soup.select('dl.hentry dt a img')
                    print(contents[0]['src']) # 글내용도 마찬가지겠지요?
                    downloadURL = 'https:' + contents[0]['src'].replace('S','L')                                  
                    print(downloadURL)
                    #download(downloadURL, os.path.join(os.getcwd(), term + '.jpg'))

                    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#                    print(result.content.decode())

                    r = requests.get(downloadURL, allow_redirects=True, headers=headers)
                    print(r)
                if not dirname == os.getcwd():              
                    ext = os.path.splitext(full_filename)[-1]
                    videos = ['.mp4','.avi','.mpg','.mpeg']
                    images = ['.jpg','.png','.jpeg']
                    if ext in videos: 
                        fsize = os.path.getsize(full_filename)
                        if fsize > 1000000000:
                            print(full_filename + " - 이동 ")
                            #shutil.move(full_filename, os.getcwd())
                    elif ext in images:
                        print(full_filename + " - 이미지 이동 ")
                        #shutil.move(full_filename, os.path.join(os.getcwd(), filename))
    except PermissionError:
        pass

search(os.getcwd())
