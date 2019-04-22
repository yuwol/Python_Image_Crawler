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
                    downloadURL = 'http://video-jav.net/wp-content/uploads/image-' + term + '.jpg'
                    print(downloadURL)
                    #download(downloadURL, os.path.join(os.getcwd(), term + '.jpg'))

                    import urllib.request
                    try:
                        urllib.request.urlretrieve(downloadURL, os.path.join(os.getcwd(), term + '.jpg')) 
                    except urllib.error.HTTPError as e:
                        print(e.__dict__)
                    except urllib.error.URLError as e:
                        print(e.__dict__)
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
