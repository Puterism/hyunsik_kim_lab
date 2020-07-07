from django.urls import path
from . import views

urlpatterns = [
    path('', views.publications, name='publications'),
    path('add/', views.publications_add, name='publications_add'),
    path('edit/<int:id>', views.publications_edit, name='publications_edit'),
    path('delete/<int:id>', views.publications_delete, name='publications_delete'),
    path('edit/order', views.publications_edit_order, name='publications_edit_order'),
]