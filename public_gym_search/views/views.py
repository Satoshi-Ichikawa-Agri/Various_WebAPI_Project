from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from public_gym_search.models.models import PublicGymnasium
from public_gym_search.serializers.serializers import PublicGymnasiumSerializer


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
