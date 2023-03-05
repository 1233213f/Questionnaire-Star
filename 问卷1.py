import random
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()

url = 'https://www.wjx.cn/vm/mx3DeJU.aspx'
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
    driver.find_element_by_xpath(f'//*[@id="div1"]/div[2]/div[{random.randint(1,2)}]/div').click()  # 男
    # '//*[@id="div1"]/div[2]/div[2]/div'  # 女
    try:
        # 2.
        driver.find_element_by_xpath(f'//*[@id="div2"]/div[2]/div[{random.randint(1,4)}]/div').click()
    except:
        pass
    # 3.
    driver.find_element_by_xpath(f'//*[@id="div3"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 4.
    driver.find_element_by_xpath(f'//*[@id="div4"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 5.
    driver.find_element_by_xpath(f'//*[@id="div5"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 6.
    driver.find_element_by_xpath(f'//*[@id="div6"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 7.
    driver.find_element_by_xpath(f'//*[@id="div7"]/div[2]/div[{random.randint(1,2)}]/div').click()
    # 8.
    driver.find_element_by_xpath(f'//*[@id="div8"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 9.
    driver.find_element_by_xpath(f'//*[@id="div9"]/div[2]/div[{random.randint(1,5)}]/div').click()
    # 10.
    driver.find_element_by_xpath(f'//*[@id="div10"]/div[2]/div[{random.randint(1,5)}]/div').click()
    # 11.
    driver.find_element_by_xpath(f'//*[@id="div11"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 12.
    driver.find_element_by_xpath(f'//*[@id="div12"]/div[2]/div[{random.randint(1,2)}]/div').click()
    # 13.
    driver.find_element_by_xpath(f'//*[@id="div13"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 14.
    driver.find_element_by_xpath(f'//*[@id="div14"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 15.
    driver.find_element_by_xpath(f'//*[@id="div15"]/div[2]/div[{random.randint(1,3)}]').click()
    # 16.
    driver.find_element_by_xpath(f'//*[@id="div16"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 17.
    driver.find_element_by_xpath(f'//*[@id="div17"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 18.
    qList_18 = [str(x) for x in range(1, 8)]  #有7个选项 range(1,8)没有8
    num = random.randint(2, 7)
    aList_18 = random.sample(qList_18, num)  # 从1，7中随机的选出 2 -> 7项
    for i in aList_18:
        xpath18 = '//*[@id="div18"]/div[2]/div[%s]' % i
        answer_18 = driver.find_elements_by_xpath(xpath18)[0]
        answer_18.click()
    # 19.
    driver.find_element_by_xpath(f'//*[@id="div19"]/div[2]/div[{random.randint(1, 5)}]/div').click()
    # 20.
    qList_20 = [str(x) for x in range(1, 6)]
    num = random.randint(2, 5)
    aList_20 = random.sample(qList_20, num)  # 从1，7中随机的选出 2 -> 5项
    for i in aList_20:
        xpath20 = '//*[@id="div20"]/div[2]/div[%s]' % i
        answer_20= driver.find_elements_by_xpath(xpath20)[0]
        answer_20.click()
    # 21.
    qList_21 = [str(x) for x in range(1, 7)]
    num = random.randint(2, 6)
    aList_21 = random.sample(qList_21, num)  # 从1，7中随机的选出 2 -> 6项
    for i in aList_21:
        xpath21 = '//*[@id="div21"]/div[2]/div[%s]' % i
        answer_21= driver.find_elements_by_xpath(xpath21)[0]
        answer_21.click()

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
    for j in range(1000):
        hpv()
        print(j)