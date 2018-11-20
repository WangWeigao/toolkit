from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stock_market_home'),
    path('avg', views.avg, name='avg'),
]
