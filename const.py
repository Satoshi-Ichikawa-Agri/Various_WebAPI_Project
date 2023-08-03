""" 定数やfunctionの管理 """
from pathlib import Path
import shutil
import time


class Const(object):
    """ 定数とfunction """

    INT_UNSET = -1  # int型valueのunset
    STRING_EMPTY = ""  # str型valueのunset

    PUBLIC_GYM_LIST_FILE = "public_gym_list.xlsx"
    PUBLIC_GYM_LIST_SHEET_NAME = "Sheet1"

    SPOLAND_URL = "https://www.homemate-research-gym.com/list/"

    WINDOWS_DOWNLOAS_DIR = "C:\\Users\\daiko\\Downloads"

    @classmethod
    def get_home_directory(cls) -> Path:
        """Get HOME directory"""
        return Path.home()

    @classmethod
    def get_current_directory(cls) -> Path:
        """Get CURRENT directory"""
        return Path.cwd()

    @classmethod
    def get_project_directory(cls) -> Path:
        """Get Project directory"""
        return cls.get_current_directory()

    @classmethod
    def file_copy(cls, original_file, copy_to):
        """File Copy"""
        shutil.copy2(original_file, copy_to)

# ====== Utility ============ #
    @classmethod
    def is_null_or_empty(cls, value):
        """指定値がNoneもしくは空でないかをチェック"""
        if value is None or value == "None":
            return True
        if len(value) == 0:
            return True
        if value == "":
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
