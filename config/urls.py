from django.contrib import admin
from django.urls import path

from public_gym_search.views.views import public_gym_search, web_scraping_execute, public_gym_register
from public_gym_search.views.home_url_views import top


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top, name='top'),
    path('public_gymnasium_search/', public_gym_search, name='public_gymnasium_search'),  # 公営体育館 検索
    path('public_gymnasium_register/', public_gym_register, name='public_gymnasium_register'),  # 公営体育館 登録
    path('public_gymnasium_scraping/', web_scraping_execute, name='public_gymnasium_scraping'),  # Scraping
]
