##Selenium安装好之后，并不能直接使用，若想使用Selenium成功调用Chrome浏览器完成相应的操作，需要通过ChromeDriver(对应当前浏览器版本)来驱动
'''https://chromedriver.storage.googleapis.com/index.html'''
#下载完成之后，解压，将其放置在Python安装路径下Scripts文件夹中即可
from selenium import webdriver
#测试能否打开浏览器
browser=webdriver.Chrome()
#打开表示成功
#打开目标网页
url=r'https://www.21cake.com/'
browser.get(url)
browser.find_element(by="上海").click()