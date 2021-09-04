#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import time
import os
import re

# 获取到需要下载音乐的网页链接

def get_url(name_list, link_list):
    url = "http://www.72dj.com/"
    headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    response = requests.get(url, headers = headers)
    res = BeautifulSoup(response.text, 'lxml')
    for k in res.find_all('a'):
#         print(k.txt)
        target = k.get('target')
        link = k.get('href')
        name = k.text
        #获取具体音乐所在网页的地址
        if link and target == "DJ_Player" and name:
            link_list.append(link)
            name_list.append(name)
            print(name)

name_list = []
link_list = []
get_url(name_list, link_list)
# print(link_list)
# print(name_list)
link_list = list(set(link_list))
name_list = list(set(name_list))



# ### 在这里发现居然是异步加载所以这里使用selenium来对其进行爬取

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

#设置浏览器关闭谷歌弹出消息
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#设置禁止图片显示，减少内存消耗和GPU
No_Image_loading = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", No_Image_loading)

browser = webdriver.Chrome('C:/Users/Noah.Suming/chromedriver.exe', chrome_options=chrome_options)
browser.maximize_window()#浏览器窗口最大化
browser.implicitly_wait(10)#隐形等待10秒

url = "http://www.72dj.com"
real_link = []
for link in link_list:
    link = url + link
    browser.get(link)
    time.sleep(random.randint(1,3))
    #获取到具体的音乐的下载地址
    down_link = browser.find_element_by_xpath("//div/audio").get_attribute('src')
    real_link.append(down_link)
    time.sleep(random.randint(1,3))
    browser.back()
browser.close()
browser.quit()

print(real_link)

# 使用urlretrieve来对其进行下载

import urllib.request
i = 0
for url in real_link:
    file_name = "music/" + str(name_list[i]).strip(".") + ".m4a"
    i = i + 1
    print(file_name)
    
    urllib.request.urlretrieve(url, file_name)
