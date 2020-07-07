from django.urls import path
from . import views

urlpatterns = [
    path('', views.professor, name='professor'),
    path('profile/edit', views.professor_profile_edit, name='professor_profile_edit'),
    path('menu/add', views.professor_menu_add, name='professor_menu_add'),
    path('menu/edit/<int:id>', views.professor_menu_edit, name='professor_menu_edit'),
    path('menu/delete/<int:id>', views.professor_menu_delete, name='professor_menu_delete'),
    path('item/add', views.professor_item_add, name='professor_item_add'),
    path('item/edit/<int:id>', views.professor_item_edit, name='professor_item_edit'),
    path('item/delete/<int:id>', views.professor_item_delete, name='professor_item_delete'),
]