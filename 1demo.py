#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def byxpath(xpath):
    return driver.find_element_by_xpath(xpath)

xpath1='//*[@id="center"]/form/table/tbody/tr/td[2]/input[1]'
xpath2='//*[@id="center"]/form/table/tbody/tr/td[2]/input[8]'
xpath3='//*[@id="center"]/form/table/tbody/tr/td[2]/input[2]'
driver=webdriver.Chrome()

try:
    driver.get('http://www.dapenti.com/blog/index.asp')
    #显性等待 10s内发现查找元素,返回true/不为null
    element=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH,xpath1)))
    driver.maximize_window()
    byxpath(xpath1).clear()
    byxpath(xpath1).send_keys('aa')
    # 普通等待
    time.sleep(2)
    byxpath(xpath2).click()
    byxpath(xpath3).click()

    #隐性等待,10s后执行下一步骤
    driver.implicitly_wait(10)

    firstURL=driver.find_element_by_xpath('//*[@id="1"]/h3').text
    print(firstURL)

finally:
    driver.quit()












