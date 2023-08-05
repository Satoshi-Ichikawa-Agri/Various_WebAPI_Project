import traceback
from django.db import transaction

from api_common.excel_operation import ExcelOperation
from const import Const
from snd_bt_search.models.models import SndBroadcast


class DataInsert(object):
    """ Data Insert """

    def __init__(self):
        """コンストラクタ"""
        pass

    def __del__(self):
        """デストラクタ"""
        print("DataInsertオブジェクトを破棄します。")

    def db_insert(self):
        """Excel to DB"""
        excel_operation = ExcelOperation()
        wb, ws = excel_operation.read_excel(
            Const.SND_LIST_FILE, Const.SND_LIST_SHEET_NAME)

        try:
            # ExcelDataを取得し、Modelリストを作成する
            model_list = []
            for row in range(2, ws.max_row + 1):
                model = SndBroadcast()
                model.broadcast_year = excel_operation.get_cell_value(ws, row, 2)
                model.broadcast_month = excel_operation.get_cell_value(ws, row, 3)
                model.broadcast_date = excel_operation.get_cell_value(ws, row, 4)
                model.broadcast_content = excel_operation.get_cell_value(ws, row, 5)
                model.assistant_1 = excel_operation.get_cell_value(ws, row, 6)
                model.assistant_2 = excel_operation.get_cell_value(ws, row, 7)
                model.guests = excel_operation.get_cell_value(ws, row, 8)
                model.remarks = excel_operation.get_cell_value(ws, row, 9)
                model_list.append(model)
            print(model_list)
            print(len(model_list))

            print("モデルリストの作成が終了した。")

            # Model → DB INSERT
            count = 0
            models = []

            with transaction.atomic():
                for model in model_list:
                    snd_broadcast = SndBroadcast(
                        broadcast_year=model.broadcast_year,
                        broadcast_month=model.broadcast_month,
                        broadcast_date=model.broadcast_date,
                        broadcast_content=model.broadcast_content,
                        assistant_1=model.assistant_1,
                        assistant_2=model.assistant_2,
                        guests=model.guests,
                        remarks=model.remarks
                        )
                    models.append(snd_broadcast)
                    count += 1

                SndBroadcast.objects.bulk_create(models)
            print(f"{ count }件のデータをINSERTしました。")

        except Exception as e:
            print(e)
            print(traceback.format_exc())
        finally:
            excel_operation.save_and_close_excel(wb)
            del excel_operation  # デストラクタの起動
