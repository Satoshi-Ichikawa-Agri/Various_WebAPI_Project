from rest_framework import serializers

from snd_bt_search.models.models import SndBroadcast


class SndBroadcastSearchSerializer(serializers.ModelSerializer):
    """SndBroadcast"""

    broadcast_year = serializers.CharField()  # 放送年yyyy
    broadcast_month = serializers.CharField()  # 放送月mm
    broadcast_date = serializers.CharField()  # 放送日YYYYmmdd
    broadcast_content = serializers.CharField()  # 放送内容
    assistant_1 = serializers.CharField()  # アシスタント1
    assistant_2 = serializers.CharField()  # アシスタント2
    guests = serializers.CharField()  # ゲスト
    remarks = serializers.CharField()  # 備考

    class Meta:
        model = SndBroadcast
        field = [
            "broadcast_year",
            "broadcast_month",
            "broadcast_date",
            "broadcast_content",
            "assistant_1",
            "assistant_2",
            "guests",
            "remarks",
        ]
        fields = "__all__"
