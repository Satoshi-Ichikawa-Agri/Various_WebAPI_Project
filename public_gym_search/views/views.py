from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from public_gym_search.models.models import PublicGymnasium
from public_gym_search.serializers.serializers import PublicGymnasiumSerializer
from .web_scraping import WebScraping


@api_view(['GET', 'POST'])
def web_scraping_execute(request):
    """ Go Scraping """
    
    if request.method == 'POST':
        
        web_scraping = WebScraping()
        web_scraping.web_scraping()
        
        return Response({
            'message': 'Response',
            'data': request.data,
            })
    
    return Response({
        'message': 'Request',
        })


@api_view(['GET', 'POST'])
def public_gym_search(request):
    """ PublicGymnasium Response View """
    
    if request.method == 'POST':
        
        prefecture = request.data['prefecture']
        municipality = request.data['municipality']
        
        queryset = PublicGymnasium.objects.filter(
            prefecture=prefecture,
            municipality=municipality
            )
        serializer = PublicGymnasiumSerializer(queryset, many=True)
        
        return Response(serializer.data)
    
    
    
    return Response({
        'message': 'あなたの住んでいる場所の公営体育館を検索できます！',
        })
