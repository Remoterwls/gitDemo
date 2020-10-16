#!usr/bin/env python
#encoding:utf-8
'''
__Author__:fusionskye
功能：
'''

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("http://172.16.1.100:8080/ezaccur/login")
# time.sleep(2)
# driver.save_screenshot('capture.png')  # 截取全屏
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div[1]/div[5]/div[2]/div/div[3]/span').click()
# ele=driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div[1]/div[5]/div[2]/div/div[3]/span')
# ActionChains(driver).move_to_element(ele).perform()
# ele = driver.find_element_by_xpath('//*[@id="yypng"]')
#
# # 获取元素位置信息
# left = ele.location['x']
# top = ele.location['y']
# right = left + ele.size['width']
# bottom = top + ele.size['height']
#
# im = Image.open('capture.png')
# im = im.crop((left, top, right, bottom))  # 元素裁剪
# im.save('ele_capture.png')  # 元素截图
#
# driver.quit()
class CrackGeetest(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()

        self.driver.get("http://172.16.1.100:8080/ezaccur/login")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div[1]/div[1]/input').send_keys('admin')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div[1]/div[2]/input').send_keys('fusion@@123')


    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div/div[3]/div[1]/div[5]/div[2]/div/div[3]/span')))
        return slider

    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        ActionChains(self.driver).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.driver).release().perform()

    def click_button(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[3]/div[1]/div[7]/input').click()

if __name__ == '__main__':
    gg = CrackGeetest()

    distance = 0
    for distance in (113,198):
        if "http://172.16.1.100:8080/ezaccur/threatPrecaution" not in gg.driver.current_url:

            slider = gg.get_slider()
            track = gg.get_track(distance)
            gg.move_to_gap(slider,track)
            gg.click_button()
            print(distance)
        else:
            print('登录成功！')
