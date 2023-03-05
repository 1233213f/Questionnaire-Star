import random
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains

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

driver.get('https://baidu.com')

a=str('//*[@id="div')
b=str('"]/div[2]/div[')
c=str(']')

l=1
# num=eval(input("输入刷问卷的次数："))
num=1
while l<=num:
    driver.get(url)
    time.sleep(1)
    # 上滑开始
    # driver.find_element_by_xpath('//*[@id="slideChunk"]').click()

    j = 1
    i = 1
    while i <= 12:#12问卷题目
        if i == 1:
            h = 4
            j = random.randint(1, h)
        elif i == 3:
            h = 2
            j = random.randint(1, h)
            if j == 2:
                i=i+1
        else:
            h = 3
            j = random.randint(1, h)
        n = a+str(i)+b+str(j)+c

        time.sleep(0)##停顿0.5秒
        driver.find_element_by_xpath(n).click()
        time.sleep(0)##停顿0.5秒
        i+=1
        try:
            driver.find_element_by_xpath('//*[@id="alert_box"]/div[2]/div[2]/button').click()
            driver.find_element_by_xpath('//*[@id="SM_BTN_1"]/div[1]/div[4]').click()
            time.sleep(2)
        except:
            time.sleep(2)
            pass
        try:
            items_ele = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')  # 滑块出现
            ActionChains(driver).drag_and_drop_by_offset(items_ele, 300, 0).perform()
        except:
            pass
        time.sleep(2)
        print(driver.title)
    l=l+1
    driver.find_element_by_xpath('//*[@id="ctlNext"]').click()


print("刷卷完成")

#div5 > div.ui-controlgroup > div:nth-child(1) > span > a
# //*[@id="div3"]/div[2]/div[1]
# //*[@id="div3"]/div[2]/div[1]
# //*[@id="div1"]/div[2]/div[1]