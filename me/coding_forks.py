#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import requests
import json



__author__ = 'yaming'
'coding project fork users'

allUsers = {}
newUsers = {}

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}

au = open('d:/keys1', encoding='utf-8')
for line in au.readlines():
    line = line.strip('\r').strip('\n')
    allUsers[line] = line

au.close()

projects = []
projects.append('https://coding.net/api/user/yaming/project/Android-Source/git/forks')
projects.append('https://coding.net/api/user/coding/project/Coding-iOS/git/forks')
projects.append('https://coding.net/api/user/coding/project/Coding-Android/git/forks')
projects.append('https://coding.net/api/user/linkin/project/mybatis-Mapper-generator/forks')
projects.append('https://coding.net/api/user/S7_V/project/kuaiqie/git/forks')

def getUsers(url):

    try:
        result = requests.get(url, headers = head).content.decode('utf-8')

        jsonResult = json.loads(result)
        code = jsonResult.get('code')
        list = jsonResult.get("data")
        # print(list)
        if code == 0 and len(list) > 0:

            for u in list:
                owner = u.get('owner')
                if owner == None:
                    continue
                key = owner.get('global_key')
                if not key in allUsers or not key in newUsers:
                    newUsers[key] = key

    except Exception as e:
        print(e)
    finally:
        pass


for url in projects:
    getUsers(url)
    print("all user: %d, new user: %d" % (len(allUsers), len(newUsers)))

r = open('d:/testkey.txt','w', encoding='utf-8')

r.write(str(newUsers))
r.close()

