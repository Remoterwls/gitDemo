#!usr/bin/env python
#encoding:utf-8
'''
__Author__:海阔天空
功能：
'''


from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('hello')
text = driver.find_element_by_id('su').get_attribute('value')

print(text)
driver.find_element_by_id('su').click()
time.sleep(2)
# driver.find_element_by_id('kw')
driver.find_element_by_id('kw').send_keys(' world')

time.sleep(2)
driver.quit()



