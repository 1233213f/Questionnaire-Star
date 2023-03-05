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

def gl5(a, b, c, d, e):
    my_list = [1] * a + [2] * b + [3] * c + [4] * d + [5] * e
    k = random.choice(my_list)
    return k

chrome_options = webdriver.ChromeOptions()
url = 'https://www.wjx.cn/vm/r9mqdpR.aspx'  ## 李坤
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
    # driver.find_element_by_xpath('//*[@id="slideChunk"]').click()
    # 1. 所在年级：
    driver.find_element_by_xpath(f'//*[@id="div1"]/div[2]/div[{random.randint(1, 5)}]/div').click()  # 男
    # //*[@id="div1"]/div[2]/div[1]/div   大一
    # 2.您的性别：
    driver.find_element_by_xpath(f'//*[@id="div2"]/div[2]/div[{random.randint(1,2)}]/div').click()
    # 3.
    driver.find_element_by_xpath(f'//*[@id="div3"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 4.
    driver.find_element_by_xpath(f'//*[@id="div4"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 5.
    driver.find_element_by_xpath(f'//*[@id="div5"]/div[2]/div[{gl3(53, 13, 34)}]/div').click()
    # 6.
    driver.find_element_by_xpath(f'//*[@id="div6"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 7.
    qList_7 = [str(x) for x in range(1, 5)]  # 有7个选项 range(1,8)没有8
    num = random.randint(1, 4)
    aList_7 = random.sample(qList_7, num)  # 从1，7中随机的选出 2 -> 7项
    for i in aList_7:
        xpath7 = '//*[@id="div7"]/div[2]/div[%s]' % i
        answer_7 = driver.find_elements_by_xpath(xpath7)[0]
        answer_7.click()

    # 8.
    qList_8 = [str(x) for x in range(1, 5)]  # 有7个选项 range(1,8)没有8
    num = random.randint(1, 4)
    aList_8 = random.sample(qList_8, num)  # 从1，7中随机的选出 2 -> 7项
    for i in aList_8:
        xpath8 = '//*[@id="div8"]/div[2]/div[%s]' % i
        answer_8 = driver.find_elements_by_xpath(xpath8)[0]
        answer_8.click()
    # 9.
    driver.find_element_by_xpath(f'//*[@id="div9"]/div[2]/div[{random.randint(1,2)}]/div').click()
    # 10.
    driver.find_element_by_xpath(f'//*[@id="div10"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 11.
    driver.find_element_by_xpath(f'//*[@id="div11"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 12.
    driver.find_element_by_xpath(f'//*[@id="div12"]/div[2]/div[{gl4(36, 25, 9, 30)}]/div').click()
    # 13.
    driver.find_element_by_xpath(f'//*[@id="div13"]/div[2]/div[{gl4(47, 35, 12, 6)}]/div').click()
    # 14.
    driver.find_element_by_xpath(f'//*[@id="div14"]/div[2]/div[{gl5(6, 39, 37, 15, 3)}]/div').click()
    # 15.
    qList_15 = [str(x) for x in range(1, 4)]  #有7个选项 range(1,8)没有8
    num = random.randint(1, 3)
    aList_15 = random.sample(qList_15, num)  # 从1，7中随机的选出 2 -> 7项
    for i in aList_15:
        xpath15 = '//*[@id="div15"]/div[2]/div[%s]' % i
        answer_15 = driver.find_elements_by_xpath(xpath15)[0]
        answer_15.click()

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
    for j in range(105):
        hpv()
        print(j)