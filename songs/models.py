from django.db import models
#комментарий для проверки
class Song(models.Model):
    CATEGORY_CHOICES = [
        ('poem', 'Стихотворение'),
        ('song', 'Песня'),
        ('story', 'Рассказ'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='poem')
    lyrics = models.TextField()
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)  # Сделали поле опциональным
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']  # Сортировка по алфавиту

    def __str__(self):
        return self.title