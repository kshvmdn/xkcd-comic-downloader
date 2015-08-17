import os
import requests
import re
import urllib.request
from bs4 import BeautifulSoup

def get_latest_comic():
    latest_comic = requests.get("http://xkcd.com/").content
    lc_soup = BeautifulSoup(latest_comic, "html.parser")

     # "Permanent link to this comic: http://xkcd.com/1564/"
    lc_string = lc_soup.find(string=re.compile("Permanent"))

    # Parse comic id from lc_link => 1564
    lc_id = int(re.search(r'\d+', lc_string).group())

    return lc_id

img_dir = os.path.expanduser("~/Desktop/xkcd_comics/")

if not os.path.exists(img_dir):
    os.mkdir(img_dir)

for i in range(0, get_latest_comic()):
    current_working_comic = requests.get("http://xkcd.com/"+str(i+1)+"/").content
    cwc_soup = BeautifulSoup(current_working_comic,"html.parser")

    cwc_img_block = cwc_soup.find("div", {"id":"comic"})
    cwc_img_tag = cwc_img_block.find("img")
    cwc_url = "http:" + cwc_img_tag["src"]

    file_path = os.path.expanduser("~/Desktop/xkcd_comics/xkcd_"+str(i+1)+".jpg")
    #print(file_path)

    if not os.path.exists(file_path):
        urllib.request.urlretrieve(cwc_url, file_path)