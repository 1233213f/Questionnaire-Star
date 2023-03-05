import random
import time

from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains

# option = ChromeOptions()
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
url = 'https://www.wjx.cn/vm/YN6yx6d.aspx'
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
    driver.find_element_by_xpath('//*[@id="slideChunk"]').click()
    # 1. 您的性别：
    driver.find_element_by_xpath(f'//*[@id="div1"]/div[2]/div[{random.randint(1,2)}]/div').click()  # 男
    # '//*[@id="div1"]/div[2]/div[2]/div'  # 女
    # 2. 你知道HPV是什么吗？
    driver.find_element_by_xpath(f'//*[@id="div2"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 3. 你了解病毒有哪些种类吗？
    for i in range(1, 5):
        driver.find_element_by_xpath(f'//*[@id="div3"]/div[2]/div[{i}]/div').click()
    # 4. HPV在人体的潜伏期可能是多久？
    driver.find_element_by_xpath(f'//*[@id="div4"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 5. 你认同男性有几率感染hpv病毒吗？
    driver.find_element_by_xpath(f'//*[@id="div5"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 6. 是否了解国内最新HPV疫苗是由厦大联合研发相关信息？
    driver.find_element_by_xpath(f'//*[@id="div6"]/div[2]/div[{random.randint(1,2)}]/div').click()
    # 7. 请问全国首个获批的人乳头瘤病毒疫苗为几价疫苗
    driver.find_element_by_xpath(f'//*[@id="div7"]/div[2]/div[{random.randint(1,4)}]/div').click()
    # 8. 你是否已经接种相关HPV疫苗？
    driver.find_element_by_xpath(f'//*[@id="div8"]/div[2]/div[{random.randint(1,2)}]/div').click()
    try:
        # 9. 你是经过怎样的途径接种疫苗？
        driver.find_element_by_xpath(f'//*[@id="div9"]/div[2]/div[{random.randint(1,5)}]/div').click()
        # 10. 你是通过什么途径了解相关疫苗接种信息呢？
        driver.find_element_by_xpath(f'//*[@id="div10"]/div[2]/div[{random.randint(1,6)}]/div').click()
        # 11. 你接种疫苗后是否有不良反应？
        driver.find_element_by_xpath(f'//*[@id="div11"]/div[2]/div[{random.randint(1,2)}]/div').click()
    except:
        pass
    # 12. 你是否有意愿或打算接种疫苗呢？
    driver.find_element_by_xpath(f'//*[@id="div12"]/div[2]/div[{random.randint(1,2)}]/div').click()
    # 13. 你觉得女性有必要接种相关hpv疫苗吗
    driver.find_element_by_xpath(f'//*[@id="div13"]/div[2]/div[{random.randint(1,2)}]/div').click()
    # 14. 你觉得学校是否有必要开展hpv疫苗知识宣传？
    driver.find_element_by_xpath(f'//*[@id="div14"]/div[2]/div[{random.randint(1,3)}]/div').click()
    # 15. 请为我国宣传疫苗力度打分？
    driver.find_element_by_xpath(f'//*[@id="div15"]/div[2]/div/ul/li[{random.randint(3,10)}]').click()
    # //*[@id="div15"]/div[2]/div/ul/li[3]/a   //*[@id="div15"]/div[2]/div/ul/li[4]/a
    # 16. 你认为当前疫苗价格是否处于接受范围？
    driver.find_element_by_xpath(f'//*[@id="div16"]/div[2]/div[{random.randint(1,5)}]/div').click()
    # 17. 你身边有哪些人接种过hpv疫苗？
    driver.find_element_by_xpath(f'//*[@id="div17"]/div[2]/div[{random.randint(1,7)}]/div').click()
    # 18. 你同意以下哪些现有疫苗接种问题的看法？（不定项）
    for i in range(1, 3):
        driver.find_element_by_xpath(f'//*[@id="div18"]/div[2]/div[{i}]/div').click()
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
    time.sleep(6)
    print(driver.title)

if __name__ == '__main__':
    driver.get('https://baidu.com')
    for j in range(10):
        hpv()
        print(j)