'''
Created on 2016-6-11

@author: jm
'''
import sqlite3

def connectNews():
    return sqlite3.connect(r'D:\Projects\NewsSpider\src\Notes\news.db')

def queryTopic(start,end):
    conn = connectNews()
    cur = conn.cursor()
    query= "SELECT Topic.Title,Topic.Link,Topic.publicDate,Sites.SiteName from Topic JOIN Sites on Topic.SiteID=Sites.SiteID ORDER BY publicDate DESC LIMIT {},{}".format(start,end)
    data = cur.execute(query).fetchall()
    for i in data:
        i = list(i)
        i[1] = 'http://www.cnbeta.com' + i[1]
        #print dict(zip(['title','link','publicDate','siteName'],i))
        yield dict(zip(['title','link','publicDate','siteName'],i))

    conn.close()

def query(sql):
    conn = connectNews()
    cur = conn.cursor()
    data = cur.execute(sql).fetchall()
    conn.close()
    
    return data

#print query("select count(*) from Topic")[0][0]
#queryTopic()