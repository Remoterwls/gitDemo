#!usr/bin/env python
#encoding:utf-8
'''
__Author__:海阔天空
功能：
'''
from PIL import Image
from io import BytesIO
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# dr = webdriver.Chrome(options=option)
# url = 'http://172.16.1.100:8080/ezaccur/login'
# dr.get(url)

driver = webdriver.Chrome()
driver.get('http://172.16.1.100:8080/ezaccur/login')
sleep(3)
driver.find_element_by_xpath("//input[@type='text']").send_keys('keyi')
driver.find_element_by_xpath("//input[@type='password']").send_keys('fusion@@123')
# move = driver.find_element_by_xpath("//div[@class='slider-btn']/span[@class='icon-wrap']")  #滑块

# driver.get_screenshot_as_png('img1')
# driver.quit()
# driver.find_element_by_xpath("//input[@type='button']").click()
# ActionChains(driver).move_to_element(button).perform()

# screenshot = driver.get_screenshot_as_png()
# screenshot = Image.open(BytesIO(screenshot))
slider = driver.find_element_by_xpath("//div[@class='slider-btn']/span[@class='icon-wrap']")
ActionChains(driver).click_and_hold(slider).perform()
sleep(5)
element = driver.find_element_by_id("YZDIVIMG")
element.screenshot('./img1.png')
print("浏览器size:", driver.get_window_size())
print("全图size:", element.size)
driver.close()