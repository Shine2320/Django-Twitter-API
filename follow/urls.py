from django.urls import path

from follow.views import home, purl, cur, durl, comp, csvs

urlpatterns = [
    path('list/', home),
    path('url/',purl),
    path('cur/',cur),
    path('durl/',durl),
    path('comp/',comp),
    path('csv',csvs)
]
