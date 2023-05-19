from rest_framework import serializers

from public_gym_search.models.models import PublicGymnasium


class PublicGymnasiumSearchSerializer(serializers.ModelSerializer):
    """ 公営体育館の検索 """
    
    prefecture = serializers.CharField() # 都道府県
    municipality = serializers.CharField() # 自治体(区市町村)
    
    class Meta:
        model = PublicGymnasium
        field = ['id', 'facility_name', 'prefecture', 'municipality', 'address', 'telephone', 'url', 'training_room_flag',]
        fields='__all__'


class PublicGymnasiumRegisterSerializer(serializers.ModelSerializer):
    """ 公営体育館の登録 """
    
    facility_name = serializers.CharField() # 施設名称
    prefecture = serializers.CharField() # 都道府県
    municipality = serializers.CharField() # 自治体(区市町村)
    address = serializers.CharField() # 所在地
    telephone = serializers.CharField() # 電話番号
    url = serializers.CharField() # HP-URL
    training_room_flag = serializers.BooleanField() # トレーニングルームの有無
    
    class Meta:
        model = PublicGymnasium
        field = ['id', 'facility_name', 'prefecture', 'municipality', 'address', 'telephone', 'url', 'training_room_flag',]
        fields='__all__'
