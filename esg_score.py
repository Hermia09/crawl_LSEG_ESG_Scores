#!/usr/bin/env python
# coding: utf-8

# In[2]:


import urllib.request    # 导入request子模块
url = 'https://www.lseg.com/en/data-analytics/sustainable-finance/esg-scores?esg=Apple+Inc#'
response = urllib.request.urlopen(url=url)  # 发送网络请求
print('响应状态码为：',response.status)
print('响应头所有信息为：',response.getheaders())
print('响应头指定信息为：',response.getheader('Accept-Ranges'))
# 读取HTML代码并进行utf-8解码
print('Python官网HTML代码如下：\n',response.read().decode('utf-8'))


# In[7]:


from bs4 import BeautifulSoup
import requests

url = 'https://www.lseg.com/en/data-analytics/sustainable-finance/esg-scores?esg=Apple+Inc#'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 以提取ESG总分为例
esg_score = soup.find('h3', class_='Heading Heading--m')
# 打印提取的数据
print(esg_score)


# In[8]:


response.status_code


# In[9]:


pip install selenium


# In[11]:


pip install webdriver_manager


# In[13]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# In[15]:


# 设置WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get('https://www.lseg.com/en/data-analytics/sustainable-finance/esg-scores?esg=Apple+Inc#')

# 等待页面加载
driver.implicitly_wait(10)

# 获取数据
esg_score_element = driver.find_element(By.CSS_SELECTOR, 'h3.Heading.Heading--m')
esg_score = esg_score_element.text

print(esg_score)


# In[26]:


# 将数据保存到CSV文件
import csv

with open('esg_score.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # 寫入标题
    writer.writerow(['Company', 'ESG Score'])
    # 写入数据
    writer.writerow(['Apple Inc', esg_score])
    


# In[27]:


import os
print(os.getcwd())


# In[ ]:


# 关闭浏览器
driver.quit()


# In[45]:


# 设置WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get('https://www.lseg.com/en/data-analytics/sustainable-finance/esg-scores?esg=Apple+Inc#')

# 等待页面加载
driver.implicitly_wait(10)

# 获取数据
esg_score_element1 = driver.find_element(By.CSS_SELECTOR, 'div.table-align-right')
esg_score = esg_score_element1.text

print(esg_score)


# In[49]:


# 设置WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get('https://www.lseg.com/en/data-analytics/sustainable-finance/esg-scores?esg=Apple+Inc#')

# 等待页面加载
driver.implicitly_wait(10)

# 获取数据
esg_score_element1 = driver.find_element(By.CSS_SELECTOR, 'div.table-align-left')
esg_score = esg_score_element1.text

print(esg_score)


# In[51]:


# 关闭浏览器
driver.quit()


# In[59]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 初始化WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.lseg.com/en/data-analytics/sustainable-finance/esg-scores?esg=Apple+Inc')

# 等待頁面元素加載
driver.implicitly_wait(10)

# 提取所有類別和分數
categories = driver.find_elements(By.CLASS_NAME, 'table-align-left')
scores = driver.find_elements(By.CLASS_NAME, 'table-align-right')

# 確保categories和scores列表長度相同
if len(categories) == len(scores):
    for i in range(len(categories)):
        category = categories[i].text
        score = scores[i].text
        print(f"Category: {category}, Score: {score}")

# 清理工作：關閉瀏覽器
driver.quit()


# In[ ]:





# In[ ]:




