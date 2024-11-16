from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from songs import views as song_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', song_views.home, name='home'),  # Главная страница
    path('about/', song_views.about, name='about'),  # Раздел "Обо мне"
    path('books/', song_views.books, name='books'),  # Раздел "Книги"
    path('cemetery/', song_views.cemetery, name='cemetery'),
    path('songs/', include('songs.urls')),  # Подключение URL-ов приложения songs
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
