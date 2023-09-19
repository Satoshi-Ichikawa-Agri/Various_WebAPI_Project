from django.db import models

from .mixin import BaseMixin


class SndBroadcast(BaseMixin):
    """SndBroadcast"""

    broadcast_year = models.CharField(max_length=4)  # 放送年yyyy
    broadcast_month = models.CharField(max_length=2)  # 放送月mm
    broadcast_date = models.CharField(max_length=8)  # 放送日YYYYmmdd
    broadcast_content = models.CharField(max_length=400)  # 放送内容
    assistant_1 = models.CharField(max_length=200)  # アシスタント1
    assistant_2 = models.CharField(max_length=200)  # アシスタント2
    guests = models.CharField(max_length=100)  # ゲスト
    remarks = models.CharField(max_length=400)  # 備考

    class Meta:
        db_table = "snd_broadcast"

    def __str__(self):
        return self.broadcast_date
