from django.shortcuts import render, get_object_or_404
from .models import Song

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cemetery(request):
    return render(request, 'cemetery.html')

def books(request):
    return render(request, 'books.html')

def songs_home(request):
    return render(request, 'songs/songs_home.html')

def poems_list(request):
    poems = Song.objects.filter(category='poem').order_by('title')  # Используйте точное значение категории из модели
    return render(request, 'songs/category_list.html', {'category_name': 'Стихотворения', 'songs': poems})

def songs_list(request):
    songs = Song.objects.filter(category='song')  # Используйте точное значение категории из модели
    return render(request, 'songs/category_list.html', {'category_name': 'Песни', 'songs': songs})

def stories_list(request):
    stories = Song.objects.filter(category='story')  # Используйте точное значение категории из модели
    return render(request, 'songs/category_list.html', {'category_name': 'Рассказы о встречах', 'songs': stories})

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    context = {
        'song': song,
        'category': song.category,  # Передаем категорию произведения
    }
    return render(request, 'songs/song_detail.html', context)

