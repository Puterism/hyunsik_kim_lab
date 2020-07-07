from django.urls import path
from . import views

urlpatterns = [
    path('', views.research_list, name='research_list'),
    path('add', views.research_add, name='research_add'),
    path('edit/<int:order>', views.research_edit, name='research_edit'),
    path('delete/<int:order>', views.research_delete, name='research_delete'),
]