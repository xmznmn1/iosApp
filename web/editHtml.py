#encoding: utf-8
from bs4 import BeautifulSoup
import sys


env = sys.argv[1]
date = sys.argv[2]
confBranch = sys.argv[3]
ipaName = '%s_%s_%s' % (date, env, confBranch)
html = "index.html"
soup = BeautifulSoup(open(html, encoding='utf-8'))
if env == 'production':
    soup.find_all(attrs='instructions')[0].string= '安装production环境包：'+ipaName
    print(soup.find_all(attrs='instructions')[0].string)
elif env == 'sandbox':
    soup.find_all(attrs='instructions')[2].string = '安装sandbox环境包：'+ipaName
    print(soup.find_all(attrs='instructions')[2].string)
elif env == 'development':
    soup.find_all(attrs='instructions')[2].string = '安装development环境包：'+ipaName
    print(soup.find_all(attrs='instructions')[2].string)
with open(html, "wb") as file:
    file.write(soup.prettify("utf-8"))