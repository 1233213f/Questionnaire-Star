import random
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random

def gl3 (a,b,c):

    my_list = [1] * a + [2] * b + [3] * c
    k = random.choice(my_list)
    return k

def gl4 (a,b,c,d):

    my_list = [1] * a + [2] * b + [3] * c + [4] * d
    k = random.choice(my_list)
    return k

def gl2(a, b):
    my_list = [1] * a + [2] * b
    k = random.choice(my_list)
    return k

def gl5(a, b, c, d, e):
    my_list = [1] * a + [2] * b + [3] * c + [4] * d + [5] * e
    k = random.choice(my_list)
    return k

chrome_options = webdriver.ChromeOptions()
url = 'https://www.wjx.cn/vm/QySpSdK.aspx'  ##
# url = 'https://www.wjx.cn/vm/mx3DeJU.aspx'
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation']) and chrome_options.add_argument('--proxy-server=http://223.82.106.253:3128') # 使用代理ip

driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

def hpv():
    driver.get(url)
    time.sleep(1)
    # 上滑开始
    driver.find_element_by_xpath('//*[@id="slideChunk"]').click()
    # 1. 您的年龄：
    time.sleep(0.5)
    driver.find_element_by_xpath(f'//*[@id="div1"]/div[2]/div[{gl2(1,1)}]/div').click()
    # //*[@id="div1"]/div[2]/div[2]/div
    # 2.您所在的年级
    # //*[@id="div2"]/div[2]/div[1]/div
    driver.find_element_by_xpath(f'//*[@id="div2"]/div[2]/div[{gl4(20,40,30,10)}]/div').click()
    # 3.

    driver.find_element_by_xpath(f'//*[@id="div3"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()

    # 4.   //*[@id="div4"]/div[2]/div[1]/div   //*[@id="div4"]/div[2]/div[2]/div
    driver.find_element_by_xpath(f'//*[@id="div4"]/div[2]/div[{gl4(1,1,1,1)}]/div').click()
    # 5.  //*[@id="div5"]/div[2]/div[1]/div  //*[@id="div5"]/div[2]/div[3]/div

    driver.find_element_by_xpath(f'//*[@id="div5"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()

    # 6.
    driver.find_element_by_xpath(f'//*[@id="div6"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()

    # 7.
    driver.find_element_by_xpath(f'//*[@id="div7"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()
    # 8.
    driver.find_element_by_xpath(f'//*[@id="div8"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()
    # 9.
    driver.find_element_by_xpath(f'//*[@id="div9"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()
    # 10.
    driver.find_element_by_xpath(f'//*[@id="div10"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()
    # 11.
    driver.find_element_by_xpath(f'//*[@id="div11"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()
    # 12.
    driver.find_element_by_xpath(f'//*[@id="div12"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()

    # 13.
    driver.find_element_by_xpath(f'//*[@id="div13"]/div[2]/div[{gl5(1,1,1,1,1)}]/div').click()
    # 14.
    driver.find_element_by_xpath(f'//*[@id="div14"]/div[2]/div[{gl4(1,1,1,1)}]/div').click()


    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="alert_box"]/div[2]/div[2]/button').click()
        driver.find_element_by_xpath('//*[@id="SM_BTN_1"]/div[1]/div[4]').click()
        time.sleep(5)
    except:
        time.sleep(2)
        pass
    try:
        items_ele = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')  # 滑块出现
        ActionChains(driver).drag_and_drop_by_offset(items_ele, 300, 0).perform()
    except:
        pass
    time.sleep(4)
    print(driver.title)

if __name__ == '__main__':
    driver.get('https://baidu.com')
    for j in range(5):
        hpv()
        print(j)