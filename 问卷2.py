from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=chrome_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

# 打开问卷主页，
def parse_page(numzz):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 1)  # 设置隐式等待时间

    driver.get(url)  # 打开url中填写的地址
    # 填写问卷

    # 性别
    xpath1 = '//*[@id="div1"]/div[2]/div[%s]' % str(random.randint(1, 2))
    answer_1 = driver.find_elements_by_xpath(xpath1)[0]
    answer_1.click()

    # 大几
    xpath2 = '//*[@id="div2"]/div[2]/div[%s]' % str(random.randint(1, 4))
    answer_2 = driver.find_elements_by_xpath(xpath2)[0]
    answer_2.click()

    # 现在是否恋爱
    xpath3 = '//*[@id="div3"]/div[2]/div[%s]' % str(random.randint(1, 2))
    answer_3 = driver.find_elements_by_xpath(xpath3)[0]
    answer_3.click()

    # 对恋爱的认知
    xpath4 = '//*[@id="div4"]/div[2]/div[%s]' % str(random.randint(1, 3))
    answer_4 = driver.find_elements_by_xpath(xpath4)[0]
    answer_4.click()

    # 对恋爱考虑的方面  多选
    qList_5 = [str(x) for x in range(1, 9)]
    num = random.randint(2, 3)
    aList_5 = random.sample(qList_5, num)  # 从1，8中随机的选出 2 -> 3项
    for i in aList_5:
        xpath5 = '//*[@id="div5"]/div[2]/div[%s]' % i
        answer_5 = driver.find_elements_by_xpath(xpath5)[0]
        answer_5.click()

    # 恋爱能接受的尺度  多选
    qList_6 = [str(x) for x in range(1, 5)]
    num = random.randint(2, 4)
    aList_6 = random.sample(qList_6, num)  # 从1，4中随机的选出 2 -> 4项
    for i in aList_6:
        xpath6 = '//*[@id="div6"]/div[2]/div[%s]' % i
        answer_6 = driver.find_elements_by_xpath(xpath6)[0]
        answer_6.click()

    # 维持的因素
    xpath7 = '//*[@id="div7"]/div[2]/div[%s]' % str(random.randint(1, 4))
    answer_7 = driver.find_elements_by_xpath(xpath7)[0]
    answer_7.click()

    # 买单
    xpath8 = '//*[@id="div8"]/div[2]/div[%s]' % str(random.randint(1, 4))
    answer_8 = driver.find_elements_by_xpath(xpath8)[0]
    answer_8.click()

    # 冲突
    xpath9 = '//*[@id="div9"]/div[2]/div[%s]' % str(random.randint(1, 3))
    answer_9 = driver.find_elements_by_xpath(xpath9)[0]
    answer_9.click()

    # 同性恋
    xpath10 = '//*[@id="div10"]/div[2]/div[%s]' % str(random.randint(1, 2))
    answer_10 = driver.find_elements_by_xpath(xpath10)[0]
    answer_10.click()

    # 家人看法
    xpath11 = '//*[@id="div11"]/div[2]/div[%s]' % str(random.randint(1, 3))
    answer_11 = driver.find_elements_by_xpath(xpath11)[0]
    answer_11.click()

    # 恋爱与婚姻关系
    xpath12 = '//*[@id="div12"]/div[2]/div[%s]' % str(random.randint(1, 5))
    answer_12 = driver.find_elements_by_xpath(xpath12)[0]
    answer_12.click()

    # 失恋
    xpath13 = '//*[@id="div13"]/div[2]/div[%s]' % str(random.randint(1, 3))
    answer_13 = driver.find_elements_by_xpath(xpath13)[0]
    answer_13.click()

    # 你如何看待异性知己
    name_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="q14"]')))  # 使用xpath查找相应的文本框的定位
    name_input.clear()  # 清楚可能存在的文本框（比如提示的框框）
    name_input.send_keys('这个是我张文琪找人填写的' + str(numzz) + '次   (*^__^*) 嘻嘻')

    # submit
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
    time.sleep(6)
    print(driver.title)
    # # # 清除缓存,退出（退出浏览器） driver.close() 关闭当前界面
    # driver.close()


if __name__ == '__main__':
    url = 'https://www.wjx.cn/m/30158090.aspx?pvw=1'

    for i in range(50000):
        parse_page(i)
        print('成功' + str(i) + '次')

