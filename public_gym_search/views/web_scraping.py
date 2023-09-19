from api_common.web_scraping import WebScrapingCommon
from const import Const


class WebScraping(object):
    """ Web Scraping """

    def __init__(self):
        pass

    def web_scraping(self):
        """"""
        wsc = WebScrapingCommon()
        driver = wsc.get_web_driver()

        global_list = []
        for page in range(1, 59):
            # 1~58p全てでスクレイピングする
            url = f"{Const.SPOLAND_URL}{ page }"
            driver.get(url)

            # 施設名称取得
            elem_target_titles = []
            elems_title = wsc.get_elements_by_classes(driver, "fa_name")
            for elem_title in elems_title:
                elem_target_titles.append(elem_title.text)

            # 住所取得
            elem_target_addresses = []
            elems_address = wsc.get_elements_by_classes(driver, "fa_address")
            for index, elem_address in enumerate(elems_address):
                elem_target_addresses.append(elem_address.text)

            # リストの中から「アクセス」要素を削除する
            delete_elem = "アクセス"
            elem_target_addresses = [item for item in elem_target_addresses if delete_elem not in item]

            # 要素の結合
            target_list = [list(items) for items in zip(elem_target_titles, elem_target_addresses)]

            global_list.append(target_list)

        wsc.disconnect(driver)
        del wsc  # デストラクタの起動

        return global_list
