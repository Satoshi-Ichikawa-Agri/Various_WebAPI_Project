"""controller"""
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from snd_bt_search.models.models import SndBroadcast
from snd_bt_search.serializers.serializers import SndBroadcastSearchSerializer
from .data_insert import DataInsert


@api_view(["GET", "POST"])
def snd_data_insert_execute(request):
    """data insert"""
    if request.method == "POST":
        # DB登録
        data_cleansing = DataInsert()
        data_cleansing.db_insert()
        print("処理が完了しました。")

        return Response({
            "message": "Response",
            "data": request.data,
            })

    return Response({
        "message": "Request",
        })


@api_view(["GET", "POST"])
def snd_broadcast_search(request):
    """ SndBroadcast Response View """
    if request.method == "POST":
        try:
            broadcast_year = request.data.get("broadcast_year")
            broadcast_month = request.data.get("broadcast_month")
            broadcast_date = request.data.get("broadcast_date")
            broadcast_content = request.data.get("broadcast_content")
            assistant_1 = request.data.get("assistant_1")
            assistant_2 = request.data.get("assistant_2")
            guests = request.data.get("guests")
            remarks = request.data.get("remarks")

            # OR条件での検索を行う
            queryset = SndBroadcast.objects.filter(
                Q(broadcast_year=broadcast_year)
                | Q(broadcast_month=broadcast_month)
                | Q(broadcast_date=broadcast_date)
                | Q(broadcast_content=broadcast_content)
                | Q(assistant_1=assistant_1)
                | Q(assistant_2=assistant_2)
                | Q(guests=guests)
                | Q(remarks=remarks)
            )
            serializer = SndBroadcastSearchSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception:
            content = {"message": "放送年、放送月、放送日、アシスタント、ゲスト、備考で検索をしてください。"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "message": "有吉弘行のSUNDAYNIGHTDREAMRの放送回を検索できます!",
    })
