#coding=utf-8
#tip:
#1.target site:http://3g.sina.com.cn/prog/wapsite/sso/,where you need to sign in
#2.parse:BeautifulSoup,which is awesome
#3.result:log in and reach your homepage,it is your work to decide what to scrap

from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import cookielib

cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
headers ={'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.114 Safari/537.36'}
#get the random infomation,include action,passwd and vk
url = 'http://3g.sina.com.cn/prog/wapsite/sso/login.php?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%D0%C2%C0%CB%CE%A2%B2%A9&vt='
keepRequest=1
logginInfo=''
while keepRequest==1:
    try:
        req = urllib2.Request(url ,headers= headers)
        logginInfo=urllib2.urlopen(req).read()
    except:
        print 'something wrong'
    else:
        keepRequest=0
soup = BeautifulSoup(logginInfo)
randomActionName=soup.form['action']
randomVkValue=soup.find(attrs={'name':'vk'})['value']
randomPasswdName=soup.find(attrs={'type':'password'})['name']
url='http://3g.sina.com.cn/prog/wapsite/sso/' + randomActionName
data={"mobile":"XX",
      randomPasswdName:'XX',
      'remember': 'on',
      'backURL': 'http://weibo.cn/',
      'vk': randomVkValue,
      'backTitle': '新浪微博',
      'submit':'登录'}
post_data=urllib.urlencode(data)
req=urllib2.Request(url,post_data,headers)
jumpPage = urllib2.urlopen(req).read()
print jumpPage
soup = BeautifulSoup(jumpPage)
jumpLink=soup.find(attrs={'class':'mg'}).contents[3]['href']
req=urllib2.Request(jumpLink,headers=headers)
finalPage=urllib2.urlopen(req).read()
soup=BeautifulSoup(finalPage)
print soup.prettify()
