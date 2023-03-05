import random
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
url = 'https://www.wjx.cn/vm/tUI32ns.aspx'
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
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
    # 1. 您的性别：
    driver.find_element_by_xpath(f'//*[@id="div1"]/div[2]/div[{random.randint(1,4)}]/div').click()  # 男
    # '//*[@id="div1"]/div[2]/div[2]/div'  # 女
    # 2.
    driver.find_element_by_xpath(f'//*[@id="div2"]/div[2]/div[{random.randint(1, 3)}]/div').click()
    # 3.
    driver.find_element_by_xpath(f'//*[@id="div3"]/div[2]/div[{random.randint(1, 2)}]/div').click()
    try:
        # 4.
        qList_4 = [str(x) for x in range(1, 5)]  # 有7个选项 range(1,8)没有8
        num = random.randint(2, 4)
        aList_4 = random.sample(qList_4, num)  # 从1，7中随机的选出 2 -> 7项
        for i in aList_4:
            xpath4 = '//*[@id="div18"]/div[2]/div[%s]' % i
            answer_4 = driver.find_elements_by_xpath(xpath4)[0]
            answer_4.click()
    except:
        pass
    # 5.
    driver.find_element_by_xpath(f'//*[@id="div5"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 6.
    driver.find_element_by_xpath(f'//*[@id="div6"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 7.
    driver.find_element_by_xpath(f'//*[@id="div7"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 8.
    driver.find_element_by_xpath(f'//*[@id="div8"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 9.
    driver.find_element_by_xpath(f'//*[@id="div9"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 10.
    driver.find_element_by_xpath(f'//*[@id="div10"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 11.
    driver.find_element_by_xpath(f'//*[@id="div11"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 12.
    driver.find_element_by_xpath(f'//*[@id="div12"]/div[2]/div[{random.randint(1,3)}]/div').click()

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
    # time.sleep(6)
    # driver.close()

if __name__ == '__main__':
    driver.get('https://baidu.com')
    for j in range(10):
        hpv()
        print(j)