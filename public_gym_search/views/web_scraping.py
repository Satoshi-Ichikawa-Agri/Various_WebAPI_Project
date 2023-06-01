from selenium import webdriver
from selenium.webdriver.common.by import By


class WebScraping(object):
    """ Web Scraping """

    def __init__(self):
        pass

    def web_scraping(self):
        """"""
        driver = webdriver.Chrome()

        global_list = []
        for page in range(1, 59):
            # 1~58p全てでスクレイピングする
            url = f'https://www.homemate-research-gym.com/list/{ page }'
            driver.get(url)

            # 施設名称取得
            elem_target_titles = []
            elems_title = driver.find_elements(By.CLASS_NAME, 'fa_name')
            for elem_title in elems_title:
                elem_target_titles.append(elem_title.text)

            # 住所取得
            elem_target_addresses = []
            elems_address = driver.find_elements(By.CLASS_NAME, 'fa_address')
            for index, elem_address in enumerate(elems_address):
                elem_target_addresses.append(elem_address.text)

            # リストの中から「アクセス」要素を削除する
            delete_elem = 'アクセス'
            elem_target_addresses = [item for item in elem_target_addresses if delete_elem not in item]

            # 要素の結合
            target_list = [list(items) for items in zip(elem_target_titles, elem_target_addresses)]

            global_list.append(target_list)

        driver.close()

        return global_list
