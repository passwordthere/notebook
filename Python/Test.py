import cookielib
import urllib2
 
url = "http://www.baidu.com"
response1 = urllib2.urlopen(url)
print ("第一种方法")
#获取状态码，200表示成功
print (response1.getcode())
#获取网页内容的长度
print (len(response1.read()))