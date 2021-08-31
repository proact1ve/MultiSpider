#!/usr/local/bin/python3

import json
import requests

## HTTP GET
r = requests.get('http://ip.dhcp.cn/?json')

##  转成 Python 字典并赋值
ip_detail = json.loads(r.text)

IP = ip_detail['IP']
ISP = ip_detail['ISP']
Country = ip_detail['Address']['Country']
Province = ip_detail['Address']['Province']
City = ip_detail['Address']['City']

## 打印
print(IP)
print(ISP)
print(Country + ',' + Province + ',' + City)
