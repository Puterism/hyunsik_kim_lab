from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('add/', views.members_add, name='members_add'),
    path('edit/<int:id>', views.members_edit, name='members_edit'),
    path('delete/<int:id>', views.members_delete, name='members_delete'),
]
