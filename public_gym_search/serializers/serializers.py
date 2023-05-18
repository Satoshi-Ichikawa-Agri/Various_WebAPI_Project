from rest_framework import serializers

from public_gym_search.models.models import PublicGymnasium


class PublicGymnasiumSerializer(serializers.ModelSerializer):
    """"""
    
    prefecture = serializers.CharField() # 都道府県
    municipality = serializers.CharField() # 自治体(区市町村)
    
    class Meta:
        model = PublicGymnasium
        field = ['id', 'facility_name', 'prefecture', 'municipality', 'address', 'telephone', 'url', 'training_room_flag',]
        fields='__all__' # 追加
