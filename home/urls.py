from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/edit', views.home_edit, name='home_edit'),
    path('setting', views.site_setting, name='site_setting'),
]