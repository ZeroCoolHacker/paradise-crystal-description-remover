from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='root_path'),
    path('normalize_description/<int:product_id>/', views.normalize_description, name='normalize_description'),
    path('normalize_all_description/', views.normalize_all_description, name='normalize_all_description'),
    path('create_collection', views.create_collection, name='create_collection'),
    path('remove_last_line', views.remove_last_line, name='remove_last_line'),
]
