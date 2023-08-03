from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class WebScrapingCommon(object):
    """WebScraping_Common"""

    def __init__(self):
        """コンストラクタ"""
        pass

    def __del__(self):
        """デストラクタ"""
        print("WebScrapingCommonオブジェクトを破棄します。")

    def get_web_driver(self, option=None):
        """"""
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        return driver

    def disconnect(self, driver):
        """"""
        driver.close()
        print("WebDriverは切断されました。")

    # ===== Selenium ==============================================================

    def get_element_by_id(self):
        """"""
        pass

    def get_element_by_class(self, driver, class_attr: str):
        """"""
        element = driver.find_element(By.CLASS_NAME, class_attr)

        return element

    def get_elements_by_classes(self, driver, class_attr: str) -> list:
        """"""
        elements = driver.find_elements(By.CLASS_NAME, class_attr)

        return elements

    def get_element_by_linktext(self, driver, class_attr: str):
        """"""
        element = driver.find_element(By.LINK_TEXT, class_attr)

        return element

    def switch_browser_tabs(self, driver):
        """"""
        driver.switch_to.window(driver.window_handles[1])

    def push_button_in_javascript(self, driver, js_code: str):
        """javascriptが埋め込まれたボタンを押下する

        サンプル:<input type="button" value="Excel" onclick="javascript:excelout()">
        """
        driver.execute_script(js_code)

    def push_link_anchor_text(self, driver, link_elem):
        """aタグのリンク(ボタン)を押下する

        サンプル:<input type="button" value="Excel" onclick="javascript:excelout()">
        """
        driver.execute_script("arguments[0].click();", link_elem)
