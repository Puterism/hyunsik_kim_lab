from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:pk>', views.article_view, name='article_view'),
    path('write', views.article_write, name='article_write'),
    path('edit/<int:id>', views.article_edit, name='article_edit'),
    path('delete/<int:id>', views.article_delete, name='article_delete'),
]