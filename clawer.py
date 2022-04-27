###################总逻辑######################
# 导入必要的库和模块
# 定义网页和请求头
# 获取html页面（字符串，注意编码问题）
# etree解析
# 观察网页源码，查看标签特征
# 编写Xpath语法，获取标签内容（文本信息末尾添加/text()）
# 存储数据（自动和zip函数）
import numpy as np
import pandas as pd
import requests
# 登录前页面
url = 'https://accounts.douban.com/passport/login'
# 请求头
headers = {
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
         }
# 账号密码
data = {
      "name":"13701712548",
      "password":"7026155@Liu",
      }
#模拟登录
session=requests.session()
session.post(url,data=data,headers=headers)
#登录成功
response=session.get("https://movie.douban.com/",headers=headers)
content=response.content.decode("utf8")

with open('douban.html','w',encoding='utf8') as f:
   f.write(content)


from lxml import etree

#字符串转换成html
html=etree.HTML(text)
#打印出来
result=etree.tostring(html,encoding='utf8').decode('utf8')

#########################Xpath##########################
text = \
"""
<ul class="ullist" padding="1" spacing="1">
    <li>
        <div id="top">
            <span class="position" width="350">职位名称</span>
            <span>职位类别</span>
            <span>人数</span>
            <span>地点</span>
            <span>发布时间</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218">python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=29938&amp;keywords=python&amp;tid=87&amp;lid=2218">python后端</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31236&amp;keywords=python&amp;tid=87&amp;lid=2218">高级Python开发工程师</a>
            </span>
            <span>技术类</span>
            <span>2</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31235&amp;keywords=python&amp;tid=87&amp;lid=2218">python架构师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34531&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34532&amp;keywords=python&amp;tid=87&amp;lid=2218">高级图像算法研发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=31648&amp;keywords=python&amp;tid=87&amp;lid=2218">高级AI开发工程师</a>
            </span>
            <span>技术类</span>
            <span>4</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32218&amp;keywords=python&amp;tid=87&amp;lid=2218">后台开发工程师</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="even">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=32217&amp;keywords=python&amp;tid=87&amp;lid=2218">Python开发（自动化运维方向）</a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
        <div id="odd">
            <span class="l square">
              <a target="_blank" href="position_detail.php?id=34511&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据挖掘讲师 </a>
            </span>
            <span>技术类</span>
            <span>1</span>
            <span>上海</span>
            <span>2018-10-23</span>
        </div>
    </li>
</ul>
"""
from lxml import  etree
#讲html字符串解析为HTML
html=etree.HTML(text)
#获取所有的div字符串
divs=html.xpath('//div')
print(divs)
#此时出现编码错误，需要解码
for div in divs:
    d=etree.tostring(div,encoding='utf8').decode('utf8')
    print(d)
    #break —— 一个debug技巧
    print("*"*50)
#获取所有id='even'的div标签
divs=html.xpath('//div[@id="even"]')
for div in divs:
    d=etree.tostring(div,encoding='utf8').decode('utf8')
    print(d)
    print("*"*50)
#获取所有a标签的herf属性的值
herf = html.xpath('//a/@href')
print(herf)
#获取div里面所有的职位信息
divs = html.xpath('//div')[1:]
print(divs)
works = []
for div in divs:
    work={}
    #获取标签的href属性
    url=div.xpath('.//a/@href')[0]  # .为当前节点下的内容，否则会出错
    #获取a标签的文本信息
    position=div.xpath('.//a/text()')[0]
    #获取工作类型
    work_type=div.xpath('.//span[2]/text()')[0]
    #获取职位人数
    work_num=div.xpath('.//span[3]/text()')[0]
    #获取工作地点
    area=div.xpath('.//span[4]/text()')[0]
    #获取发布时间
    time = div.xpath('.//span[5]/text()')[0]
    work={
        "url":url,
        "position":position,
        "work_type":work_type,
        "work_num":work_num,
        "area":area,
        "time":time,
    }
    works.append(work)
with open("text",'w',encoding='utf8') as f:
    f.write(works)


###爬豆瓣##########################
import requests
from lxml import   etree
# 获取URL
urls = []
for i in range(0,5,1):
    i = i*20
    url = 'https://movie.douban.com/review/best/?start={}'.format(i) #string的用法
    urls.append(url)
# 获取每一页url中每个影评的url
headers = {
   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
         }
detail_urls=[]
for url in urls:
    # 发送请求
    response=requests.get(url,headers=headers)
    #编码转换
    content=response.content.decode('utf8')
    #解析html字符串
    html=etree.HTML(content)
    #Xpath提取每个电影的href
    detail_url = html.xpath('//h2/a/@href')
    detail_urls.append(detail_url)

# 获取电影影评的数据
movies=[]
for page in detail_urls:
    for url in page:
        try:
        #发送请求
            response=requests.get(url,headers=headers)
            content = response.content.decode('utf8')
            html = etree.HTML(content)
            #抓取电影名
            title=html.xpath('//div[@class="subject-title"]/a/text()')[0][2:]
            print('正在爬取电影：{}'.format(title))
            #抓取评论者和评分
            commenter = html.xpath('//header/a/span/text()')[0]
            if len(html.xpath('//header//span/@title'))!=0:
                rank = html.xpath('//header//span/@title')[0]
            else:
                rank="None"
            comment=html.xpath('//div[@id="link-report"]//p/text()')
            comment=''.join(comment)
            movie={
                'title':title,
                'commenter':commenter,
                'rank':rank,
                'comment':comment,
            }
            movies.append(movie)
        except Exception as e:
            print(e)


###############正则表达式#############
import re
#match 是从起始位置开始匹配
#“.”匹配任意字符
#”\n“换行符 . 不能匹配
#“\d”匹配任意数字
#“\D”匹配数字外任意字符
#“\s”匹配空白字符（“\n,\t,\r \s”）
#“\w”匹配任意字母，数字和下划线
#“\W ”除了“\w”之外的
#[]组合的方式，只要在中括号内均可匹配
#* 匹配无数个包括0 + 匹配1或多个 ?   要么0要么1  {n}  匹配n次 {m,n} 匹配 m到n个



######东方财富网   带有ajax的爬虫###########


names=[]
codes=[]
for i in range(250):
    print(i)
    url='http://56.push2.eastmoney.com/api/qt/clist/get?cb=' \
        'jQuery112409916829584199305_1650544998156&pn={}&pz=20&po=1&np' \
        '=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=' \
        'f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=' \
        'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,' \
        'f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1650544998157'.format(i)

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
    response=requests.get(url,headers=headers)
    content = response.content.decode('utf8')

    ####只能用正则表达式了###############
    #个股名称
    all_names = re.findall('f14\D+',content)
    all_code = re.findall('f12\D{3}\w+',content)
    for n,c in zip(all_names,all_code):
        codes.append(c.replace('f12":"',""))
        names.append(n.replace('f14":"',"").replace('","f',""))
import pandas as pd
data=pd.DataFrame(names,index=codes,columns=['names'])


#############格隆汇专栏  flex布局（翻页的都要正则表达）################################
import requests
from lxml import etree
import pandas as pd
import re
import numpy as np

titles=[]
hrefs=[]
for i in range(10):
    url = 'https://www.gelonghui.com/api/columnArticle/getSelected?page={}&count=16&version=2'.format(i+1)

    headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
            }
    response = requests.get(url, headers=headers)
    content = response.content.decode('utf8')
    title = re.findall('title":"[\u4e00-\u9fa50-9\uff0c\u3001\uff1a\u201c\u201d；！.\s]+',content)
    href = re.findall('postId":[0-9]+', content)
    href_d=[]
    x=[]
    for h in href:
        if x==h:
            continue
        else:
            href_d.append(h)
            x=h
    if len(href_d)==len(title):
        for h,t in zip(href_d,title):
            titles.append(t.replace('title":"',''))
            print(t.replace('title":"',''))
            hrefs.append('https://www.gelonghui.com/p/{}'.format(h.replace('postId":','')))

data = pd.DataFrame(list(zip(titles,hrefs)))

page_url = 'https://www.gelonghui.com/p/523119'
page_response = requests.get(page_url, headers=headers)
page_content = page_response.content.decode('utf8')
page_html = etree.HTML(page_content)
x = page_html.xpath('//p/text()')


#########################微信小程序的爬虫######################################

