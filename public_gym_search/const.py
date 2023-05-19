""" 定数やfunctionの管理 """
import os
import time
from datetime import date, datetime


class Const(object):
    """ 定数とfunction """
    
    GYM_SITE_URL = 'https://www.homemate-research-sports.com/'
    
    WORKSPACE_DIR = os.getcwd() # workspaceのdirectory_path
    
    INT_UNSET = -1 # int型valueのunset
    STRING_EMPTY = '' # str型valueのunset


    @classmethod
    def is_null_or_empty(cls, value):
        """指定値がNoneもしくは空でないかをチェックする
        """
        if value is None or value == 'None':
            return True
        if len(value) == 0:
            return True
        if value == '':
            return True
        
        return False


    @classmethod
    def remove_value(cls, value, start, end):
        """ 指定した範囲の文字列を削除する
        Parameters:
            value: 対象の値
            start: 開始位置
            end: 終了位置
        """
        return value[:start] + value[end + 1:]


    @classmethod
    def time_keeper(cls, seconds: int):
        """ Time Keeper """
        time.sleep(seconds)

