import os
from selenium import webdriver # Selenium Web自動操作
from selenium.webdriver.common.by import By # HTML要素の検索

from const import Const


class WebScraping(object):
    """ Web Scraping """
    
    def __init__(self):
        pass


    def web_scraping(self):
        """"""
        driver = webdriver.Chrome()
        driver.get(Const.GYM_SITE_URL)
        Const.time_keeper(2)
        
        target_elem = driver.find_element(By.CLASS_NAME, '')
        target_link = driver.find_element(By.LINK_TEXT, '')
        
        driver.close()
        return
