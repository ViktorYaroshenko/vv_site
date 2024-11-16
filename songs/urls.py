from django.urls import path
from . import views

urlpatterns = [
    path('', views.songs_home, name='songs_home'),  # Общий раздел песен и произведений
    path('poems/', views.poems_list, name='poems_list'),  # Стихотворения
    path('songs/', views.songs_list, name='songs_list'),  # Песни
    path('stories/', views.stories_list, name='stories_list'),  # Рассказы о встречах
    path('<int:pk>/', views.song_detail, name='song_detail'),  # Детальная страница произведения
]