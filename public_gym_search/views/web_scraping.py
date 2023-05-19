import os
from selenium import webdriver # Selenium Web自動操作
from selenium.webdriver.common.by import By # HTML要素の検索

from public_gym_search.const import Const


class WebScraping(object):
    """ Web Scraping """
    
    def __init__(self):
        pass


    def web_scraping(self):
        """"""
        driver = webdriver.Chrome()
        driver.get(Const.GYM_SITE_URL)
        Const.time_keeper(2)
        
        target_elem_is_prefmap = driver.find_element(By.CLASS_NAME, 'mod_prefmap_srch')
        target_link = driver.find_element(By.LINK_TEXT, '')
        
        driver.close()
        return
