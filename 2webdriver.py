import time
import lxml.etree
from fake_useragent import UserAgent
from selenium import webdriver
import requests
from selenium.webdriver.support.ui import WebDriverWait

try:
    browser = webdriver.Chrome()
    browser.get('https://weixin.sogou.com/')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="query"]').send_keys('晚情')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="searchForm"]/div/input[3]').click()
    time.sleep(3)
    original_handle=browser.current_window_handle
    for j in range(2,10):
        for i in range(10):
            browser.find_element_by_xpath(f'//*[@id="sogou_vr_11002601_title_{i}"]').click()
            handles = browser.window_handles
            for handle in handles:
                if handle != browser.current_window_handle:
                    browser.switch_to.window(handle)
            time.sleep(3)
            title = browser.find_element_by_xpath('//*[@id="activity-name"]').text
            print(title)
            time.sleep(3)
            content = browser.find_element_by_xpath('//*[@id="js_content"]').text
            print(content)
            with open(f'content{(j-2)*10+i+1}.txt', 'w+', encoding='utf-8') as f:
                f.write(title)
                f.write(content)
            browser.switch_to.window(original_handle)
        browser.find_element_by_xpath(f'//*[@id="sogou_page_{j}"]').click()
        time.sleep(3)

    for i in range(1):
        browser.find_element_by_xpath(f'//*[@id="sogou_vr_11002601_title_{i}"]').click()
        handles = browser.window_handles
        for handle in handles:
            if handle != browser.current_window_handle:
                browser.switch_to.window(handle)
        time.sleep(3)
        title = browser.find_element_by_xpath('//*[@id="activity-name"]').text
        print(title)
        time.sleep(3)
        content = browser.find_element_by_xpath('//*[@id="js_content"]').text
        print(content)
        with open(f'content{i}.txt', 'w+', encoding='utf-8') as f:
            f.write(title)
            f.write(content)
        browser.switch_to.window(original_handle)

    time.sleep(3)

except Exception as e:
    print(e)
finally:
    pass
