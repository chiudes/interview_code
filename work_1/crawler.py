#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json
import os
import subprocess

my_options = webdriver.ChromeOptions()
my_options.add_argument("--start-maximized")         #最大化視窗
my_options.add_argument("--incognito")               #開啟無痕模式
my_options.add_argument("--disable-popup-blocking") #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消通知
my_options.add_argument("--lang=zh-TW")  #設定為繁體中文

driver_exec_path = "./chromedriver.exe"

driver = webdriver.Chrome(
    options = my_options,
    executable_path = driver_exec_path
)

list_num = [1,2,3,7,14]
def visit():
    driver.get('https://plvr.land.moi.gov.tw/DownloadOpenData')
    
def click():
    driver.find_elements(
        By.CSS_SELECTOR,
        "div li.ui-state-default.ui-corner-top"
    )[1].click()
    sleep(2)
    
    driver.find_element(
        By.CSS_SELECTOR,
        'tr select#historySeason_id option[value="108S2"]'
    ).click()
    sleep(2)
    
    driver.find_element(
        By.CSS_SELECTOR,
        'tr select#fileFormatId option[value="csv"]'
    ).click()
    sleep(2)
    
    driver.find_element(
        By.CSS_SELECTOR,
        'font label[for="downloadTypeId2"]'
    ).click()
    sleep(2)
    
    for i in list_num:
        driver.find_elements(
            By.CSS_SELECTOR,
            'td.form_intro input.checkBoxGrp.landTypeA'
        )[i].click()
    sleep(2)
    
    driver.find_element(
        By.CSS_SELECTOR,
        'td.form_gray input#downloadBtnId'
    ).click()
    sleep(15)

def close():
    driver.quit()

if __name__ == "__main__":
    visit()
    click()
    close()