from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('1', views.index, name='index'),
    path('2', views.index_2, name='index_2'),
    path('characters/<int:id>/', views.characters, name='characters'),
    path('locations/<int:id>/', views.locations, name='locations'),
    path('episodes/<int:id>/', views.episodes, name='episodes'),
    ]
