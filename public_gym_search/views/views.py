from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from public_gym_search.models.models import PublicGymnasium
from public_gym_search.serializers.serializers import (
    PublicGymnasiumSearchSerializer,
    PublicGymnasiumRegisterSerializer
    )
from .web_scraping import WebScraping
from .data_cleansing import DataCleansing


@api_view(["GET", "POST"])
def web_scraping_execute(request):
    """ Go Scraping """
    if request.method == "POST":

        # スクレイピング
        web_scraping = WebScraping()
        gym_list = web_scraping.web_scraping()

        # データクレンジング
        data_cleansing = DataCleansing(gym_list)
        data_cleansing.data_cleansing_process()

        # データクレンジングpart2
        data_cleansing.data_cleansing_address()

        # DB登録
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
def public_gym_search(request):
    """ PublicGymnasium Response View """
    if request.method == "POST":
        try:
            prefecture = request.data.get("prefecture")
            municipality = request.data.get("municipality")

            # OR条件での検索を行う
            queryset = PublicGymnasium.objects.filter(
                Q(prefecture=prefecture) | Q(municipality=municipality)
            )
            serializer = PublicGymnasiumSearchSerializer(queryset, many=True)

            return Response(serializer.data)

        except Exception:
            content = {"message": "都道府県もしくは区市町村で検索をしてください。"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "message": "あなたの住んでいる場所の公営体育館を検索できます！",
    })


@api_view(["GET", "POST"])
def public_gym_register(request):
    """ PublicGymnasium Register View """
    if request.method == "POST":
        try:
            serializer = PublicGymnasiumRegisterSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    queryset = PublicGymnasium.objects.all()
    serializer = PublicGymnasiumSearchSerializer(queryset, many=True)

    return Response({
        "message": "新規公営体育館を登録します。",
        "data": serializer.data,
        })
