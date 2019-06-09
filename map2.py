import requests
import json
from requests.adapters import *
import requests.adapters

def get_place(place):
    url = "http://api.map.baidu.com/place/v2/search?query="
    myak = "&region=西安&output=json&ak=gPItzAVKUHLXAGcVgIzGMOz8PsZKzGdY"
    all_url = url+place+myak
    print(all_url)
    #  这里设置请求最大次数，如果失败，再次发起请求
    timeout = 500
    socket.setdefaulttimeout(timeout)  # 设置超时
    requests.adapters.DEFAULT_RETRIES = 5
    i = 5
    while i>0:
        try:
            req = requests.get(all_url)
            content = json.loads(req.text)
            if content["status"] != 0:
                print(content["status"])
                return 0
            return content["results"]
        except:
            i = i-1
    return 0

def get_park(location):
    url = "http://api.map.baidu.com/place/v2/search?query=停车场&location="
    myak = "&radius=2000&output=json&ak=gPItzAVKUHLXAGcVgIzGMOz8PsZKzGdY"
    all_url = url + location + myak
    timeout = 500
    socket.setdefaulttimeout(timeout)  # 设置超时
    requests.adapters.DEFAULT_RETRIES = 5
    i = 5
    while i > 0:
        try:
            req = requests.get(all_url)
            content = json.loads(req.text)
            if content["status"] != 0:
                print(content["status"])
                return 0
            return content["results"]
        except:
            i = i - 1
    return 0

def get_distance(origins,destinations):
    url="http://api.map.baidu.com/direction/v2/driving?output=json&origin="
    link = "&destination="
    myak = "&output=json&ak=gPItzAVKUHLXAGcVgIzGMOz8PsZKzGdY"
    all_url = url + origins + link + destinations + myak
    timeout = 500
    socket.setdefaulttimeout(timeout)  # 设置超时
    requests.adapters.DEFAULT_RETRIES = 5
    i = 5
    while i > 0:
        try:
            req = requests.get(all_url)
            content = json.loads(req.text)
            if content["status"] != 0:
                print(content["status"])
                return 0
            return content['result']['routes']
        except:
            i = i - 1
    return 0

def link(origins):
    data = get_park(origins)
    for i in data:
        lat = i["location"]["lat"]
        lng = i["location"]["lng"]
        destinations = "%f,%f"%(lat,lng)
        result = get_distance(origins,destinations)[0]
        i["distance"] = result['distance']
        i["duration"] = result['duration']
    return data
