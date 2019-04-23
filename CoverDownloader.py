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
                #search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                videos = ['.mp4','.avi','.mpg','.mpeg']
                if ext in videos: 
                    term = os.path.splitext(filename)[0]
                    if(os.path.exists(os.path.join(os.getcwd(), term.upper() + '.jpg'))):
                        print(term.upper() + ' - exists')
                    else:
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
    except PermissionError:
        pass

search(os.getcwd())
