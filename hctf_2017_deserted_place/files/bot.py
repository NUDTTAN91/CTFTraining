#!/usr/bin/env python
# -*- coding:utf-8 -*-

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import os
import time
import requests

url = "http://127.0.0.1:80/"

username = "hctf_admin_LoRexxar2e23"
password = "123456"

while 1:
    try:
        # Alpine
        # apk add chromium chromium-chromedriver
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1024,768")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-software-rasterizer")
        chrome_options.add_argument("--disable-default-apps")
        browser = webdriver.Chrome(chrome_options=chrome_options)

        print "[INFO] Start New Round..."

        browser.set_page_load_timeout(10)
        browser.set_script_timeout(10)

        # print "[INFO] [+] logout..."
        browser.get(url + '/logout.php')
        time.sleep(1)

        # print "[INFO] [+] login..."
        browser.get(url + '/login.php')
        time.sleep(2)

        elem = browser.find_element_by_name("user")
        elem.clear()
        elem.send_keys(username)
        elem = browser.find_element_by_name("pass")
        elem.clear()
        elem.send_keys(password)
        elem = browser.find_element_by_name("submit")
        elem.click()

        # print "[INFO] [+] getmess..."
        browser.get(url + '/api/getmess.php')

        while 1:
            try:
                browser.switch_to_alert().accept()  # 接收一切弹框，防止浏览器被弹框
            except selenium.common.exceptions.NoAlertPresentException:
                break

        source = browser.page_source

        if "Nothing" not in source:
            print time.strftime("%Y-%m-%d %X", time.localtime())
            print "\033[1;31m[S] Reading now...\033[0m"
            print(source)
            time.sleep(5)
            browser.get(url + '/api/clearmess.php')
            browser.quit()
            time.sleep(1)

        if "This is not where you should come" in source:
            print time.strftime("%Y-%m-%d %X", time.localtime())
            print "[INFO] bot admin check error..."
            browser.quit()
            time.sleep(2)
        else:
            print time.strftime("%Y-%m-%d %X", time.localtime())
            print "[INFO] no unread messages..."
            browser.quit()
            time.sleep(2)
            # exit(0)

    except Exception as e:
        print "[ERROR] " + str(e)
        time.sleep(2)
        browser.quit()
