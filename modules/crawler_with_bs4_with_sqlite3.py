#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sqlite3
import datetime

# 设置要抓取的总页数
#ALL_PAGE_NUMBER = 21
ALL_PAGE_NUMBER = 1

# 保存到本地Sqlite
def saveToSqlite(lesson_info):
    # 获取lesson_info字典中的信息
    name = lesson_info['name']
    link = lesson_info['link']
    des = lesson_info['des']
    time = lesson_info['time']
    degree = lesson_info['degree']

    # 连接数据库并插入相应数据
    con = sqlite3.connect("lesson.db")
    cur = con.cursor()

    #运行创建表格一次，然后注释掉，否则会报错
    #cur.execute("create table lesson_xx(name varchar(10),link TEXT,des TEXT,time varchar(30),degree varchar(10))")
    sql = "insert into lesson_xx values ('%s', '%s','%s','%s','%s')" % (name, link, des, time, degree)
    cur.execute(sql)
    con.commit()

# 抓取主函数
def startGrab():
    # 所有课程页面的BaseURL
    base_url = 'http://www.jikexueyuan.com/course/?pageNum='
    # 当前页码
    page_number = 1

    name=''
    link=''
    des=''
    time=''
    degree=''
    

    while page_number <= ALL_PAGE_NUMBER:
        url = base_url + str(page_number)
        print ">>>>>>>>>>>将要抓取", url

        # 可能因为超时等网络问题造成异常，需要捕获并重新抓取
        try:
            page = requests.get(url)
        except:
            print "重新抓取 ", url
            continue

        # 使用BeautifulSoup规范化网页并生成对象
        #soup = BeautifulSoup(open('sourse.html'),'lxml')
        soup = BeautifulSoup(page.content,'lxml')

        lesson_data = soup.find_all("li")
        for item in lesson_data:
            lessons=item.find_all('h2')
            lessons_desc=item.find_all('p')
            lessons_time=item.find_all('dd',{'class':'mar-b8'})
            lessons_c=item.find_all('dd',{'class':'zhongji'})
            for lesson in lessons:
                lesson_info=lesson.find('a')
 #               print lesson_info.get('href'),lesson_info.string
                name = lesson_info.string
                link = lesson_info.get('href')
            for lesson_time in lessons_time:
#                print lesson_time
                lesson_t=lesson_time.find('em').string
#                print lesson_t
                time = lesson_t
            for c in lessons_c:
                lesson_c=c.find('em').string
#                print lesson_c
                degree = lesson_c
            for d in lessons_desc:
                lesson_desc=d.string
#                print lesson_desc
                des = lesson_desc
            lesson_info = {"name": name, "link": link, "des": des, "time": time, "degree": degree}
            if lesson_info['name']:
                saveToSqlite(lesson_info)

            page_number = page_number + 1


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    startGrab()
    endtime = datetime.datetime.now()
    print "执行时间: ", (endtime - starttime).seconds, "s"
