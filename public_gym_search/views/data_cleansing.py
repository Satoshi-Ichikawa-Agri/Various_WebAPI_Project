import os
import re
from openpyxl import load_workbook

from public_gym_search.const import Const


class GymExcelModel(object):
    """ スクレイピング結果→Excel """
    
    def __init__(self):
        self.index = Const.INT_UNSET # for文のindex用
        
        self.facility_name = Const.STRING_EMPTY
        self.prefecture = Const.STRING_EMPTY
        self.municipality = Const.STRING_EMPTY
        self.address = Const.STRING_EMPTY
        self.telephone = None
        self.url = None
        self.training_room_flag = None
        


class DataCleansing(object):
    """ Data Cleansing """
    
    def __init__(self, data_list):
        self.data_list = data_list # スクレイピング結果オブジェクト
        self.wb = load_workbook('public_gym_list.xlsx') # Excel Book
        self.ws = self.wb['Sheet1'] # Excel Sheet


    def get_value(self, column, row):
        """ 対象セルの値を取得する """
        if column < 0 or row < 0:
            return ''
        
        value = str(self.ws.cell(row=row, column=column).value)
        
        if Const.is_null_or_empty(value):
            return ''
        
        return value
    
    
    def set_value(self, column, row, value):
        """ 対象セルに値をセットする """
        self.ws.cell(column=column, row=row).value = value


    def remove_date(self, value):
        """ 豚肉相場一覧表_yyyymm.xlsxの「全国と畜頭数」列の値が
        数値と日付の情報となっているので、日付を削除する処理
        変更前: 68800 (2023/02/28)
        変更後: 68800
        """
        # 正規表現
        regex = r'\(\d{4}/\d{1,2}/\d{1,2}\)'
        # 正規表現で示して値だけ削除し、さらに空白を削除する
        removed_value = str.strip(re.sub(regex, '', value))
        
        return removed_value


    def data_cleansing_process(self):
        """ データクレンジング処理 """
        model_list = []

        for i, element in enumerate(self.data_list):
            for j, sublist in enumerate(element):
                model = GymExcelModel()
                for k, item in enumerate(sublist):
                    if k == 0:
                        model.facility_name = item
                    if k == 1:
                        model.address = item
                else:
                    model_list.append(model)
                    
        
        print(len(model_list))
        
        # Excel 書込み
        for i, model in enumerate(model_list):
            i += 1
            self.ws.cell(row=i, column=1).value = model.facility_name
            self.ws.cell(row=i, column=2).value = model.address
        

        print('処理が完了しました')
        self.wb.save('public_gym_list.xlsx')
        self.wb.close()
