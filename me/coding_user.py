#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'coding users'

import requests
import pymysql.cursors
import time
import json

__author__ = 'yaming'

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}

allUsers = {}

allUsers['coding'] = 'coding'

requestUsers = {}

u = open('d:/keys')
for line in u.readlines():
    k = line.strip('\n').strip('\r')
    allUsers[k] = k

u = open('d:/keys1')
for line in u.readlines():
    k = line.strip('\n').strip('\r')
    if k not in allUsers:
        requestUsers[k] = k

count = 0




def getUserInfo(nick):

    allUsers[nick] = nick

    url = 'https://coding.net/api/user/friends/%s?page=1&pageSize=1000' % nick
    print(url)

    jsonContent = requests.get(url, headers = head).content.decode('utf-8')
    jsDict = json.loads(jsonContent)
    code = jsDict.get('code')
    list = jsDict.get("data")['list']
    # print(list)
    if code == 0 and len(list) > 0:

        for u in list:
            id = u.get('id')
            name = u.get('name')
            name_pinyin = u.get('name_pinyin')
            tags_str = u.get('tags_str')
            job_str = u.get('job_str')
            job = u.get('job')
            birthday = u.get('birthday')
            location = u.get('location')
            company = u.get('company')
            slogan = u.get('slogan')
            introduction = u.get('introduction')
            avatar = u.get('avatar')
            gravatar = u.get('gravatar')
            lavatar = u.get('lavatar')
            created_at = u.get('created_at')
            last_logined_at = u.get('last_logined_at')
            last_activity_at = u.get('last_activity_at')
            global_key = u.get('global_key')
            updated_at = u.get('updated_at')
            path = u.get('path')
            status = u.get('status')
            is_member = u.get('is_member')
            points_left = u.get('points_left')
            follows_count = u.get('follows_count')
            fans_count = u.get('fans_count')
            tweets_count = u.get('tweets_count')
            phone_country_code = u.get('phone_country_code')
            country = u.get('country')
            followed = u.get('followed')
            follow = u.get('follow')
            sex = u.get('sex')
            tags = u.get('tags')

            conn = pymysql.connect(host = '123.56.103.190',
                                   user = 'root',
                                   password = 'AlpkQwer4321' ,
                                   charset = 'utf8mb4' ,
                                   cursorclass=pymysql.cursors.DictCursor)
            conn.select_db('gold')
            try:
                with conn.cursor() as cursor:
                    # query
                    selectSql = "select id, name from followers WHERE  global_key='%s'" % global_key
                    cursor.execute(selectSql)

                    result = cursor.fetchone()
                    if result != None or '@qq' in global_key:
                        continue
                if not global_key in requestUsers and not global_key in allUsers:
                    requestUsers[global_key] = global_key

                with conn.cursor() as cursor:
                    # Create a new user record
                    createSql = "INSERT INTO  followers(id, name,name_pinyin,tags_str,job_str," \
                                "job,birthday,location,company,slogan,introduction,avatar,gravatar,lavatar,created_at,last_logined_at," \
                                "last_activity_at,global_key,updated_at,path,status,is_member,points_left," \
                                "follows_count,fans_count,tweets_count,phone_country_code,country,followed,follow,sex,tags) " \
                                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"

                    cursor.execute(createSql, (str(id), str(name), str(name_pinyin), str(tags_str), str(job_str), str(job), str(birthday), str(location), str(company),
                                               str(slogan), str(introduction), str(avatar), str(gravatar), str(lavatar), str(created_at), str(last_logined_at),
                                               str(last_activity_at), str(global_key), str(updated_at), str(path), str(status), str(is_member), str(points_left),
                                               str(follows_count), str(fans_count), str(tweets_count), str(phone_country_code), str(country), str(followed), str(follow), str(sex), str(tags)))

                conn.commit()

            except pymysql.Error as e:
                print(e)
                print(u)
            finally:
                conn.close()
                time.sleep(0.1)
        print("success: %s", nick)

    else:
        print("request error")

    data = requestUsers.popitem()
    print("requestUser size: %d, allUser size: %d" % (len(requestUsers), len(allUsers)))
    if len(data) > 0:
        getUserInfo(data[0])


def test():
    count = round(100) + 1
    requestUsers['test' + str(count)] = 'i' + str(count)


# getUserInfo(requestUsers.popitem().index(0))
# print(requestUsers.popitem().index(0))
data = requestUsers.popitem()
getUserInfo(data[0])
print(data)
print(data[0])
# for n, value in data.items():
#     print("n: %s, value:%s " % (n, value))
    # test()
    # getUserInfo(n)
    # time.sleep(0.1)


