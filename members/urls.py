from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('add/', views.members_add, name='members_add'),
    path('edit/<int:id>', views.members_edit, name='members_edit'),
    path('delete/<int:id>', views.members_delete, name='members_delete'),
    path('position/add', views.position_add, name='position_add'),
    path('position/edit/<int:id>', views.position_edit, name='position_edit'),
    path('position/delete/<int:id>', views.position_delete, name='position_delete'),
]
