from django.contrib import admin
from django.urls import path

from public_gym_search.views.views import (
    public_gym_search,
    web_scraping_execute,
    public_gym_register,
    data_insert_execute,
)
from public_gym_search.views.home_url_views import top
from snd_bt_search.views.views import snd_broadcast_search, snd_data_insert_execute, snd_search


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", top, name="top"),
    # ----- API ----- #
    path("public_gymnasium_search/", public_gym_search, name="public_gymnasium_search"),  # 公営体育館 検索api
    path("public_gymnasium_register/", public_gym_register, name="public_gymnasium_register"),  # 公営体育館 登録api
    path("public_gymnasium_scraping/", web_scraping_execute, name="public_gymnasium_scraping"),  # Scrapingapi
    path("public_gymnasium_data_insert/", data_insert_execute, name="public_gymnasium_insert"),  # insertapi
    path("snd_broadcast_insert/", snd_data_insert_execute, name="snd_data_insert_execute"),  # SNDのinsertapi
    path("snd_broadcast_search/", snd_broadcast_search, name="snd_broadcast_search"),  # SNDの検索api
]
