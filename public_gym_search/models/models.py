from django.db import models
from django.utils.crypto import get_random_string

from .mixin import BaseMixin


def create_primary_key():
    """ ランダムな12桁の文字列を生成 """
    
    return get_random_string(12)


class PublicGymnasium(BaseMixin):
    """ PublicGymnasium """
    
    id = models.CharField(default=create_primary_key(), primary_key=True, max_length=12) # 主キー
    facility_name = models.CharField(max_length=100, unique=True) # 施設名称
    prefecture = models.CharField(max_length=20) # 都道府県
    municipality = models.CharField(max_length=20) # 自治体(区市町村)
    address = models.CharField(max_length=255) # 所在地
    telephone = models.CharField(max_length=30) # 電話番号
    url = models.CharField(max_length=255) # HP-URL
    training_room_flag = models.BooleanField() # トレーニングルームの有無
    
    class Meta:
        db_table = 'public_gymnasium'
        ordering = ['prefecture']
    
    def __str__(self):
        return self.facility_name
