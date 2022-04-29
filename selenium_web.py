##Selenium安装好之后，并不能直接使用，若想使用Selenium成功调用Chrome浏览器完成相应的操作，需要通过ChromeDriver(对应当前浏览器版本)来驱动
'''https://chromedriver.storage.googleapis.com/index.html'''
#下载完成之后，解压，将其放置在Python安装路径下Scripts文件夹中即可
from selenium import webdriver
from selenium.webdriver.common.by import By
#测试能否打开浏览器
driver=webdriver.Chrome()
#打开表示成功
#打开目标网页
url = r'https://www.baidu.com/'
driver.get(url)
driver.title
'''可以查找的元素类型有8类
NAME,ID,XPATH,CLASS_NAME,CSS_SELECTOR,LINK_TEXR,PARTIAL_LINK_TEXT,TAG_NAME'''
search_box = driver.find_element(By.NAME, "wd")
search_button = driver.find_element(By.ID, "su")
'''对元素可以进行的操作
填写 send_keys
点击 .click()
'''
search_box.send_keys("Selenium")
search_button.click()
driver.find_element(By.NAME, "q").get_attribute("value") # => "Selenium"
driver.quit()

