from django.db import models

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name='Жанр')

    def __str__(self):
        return self.title

class Country(models.Model):
    title = models.CharField(max_length=100, verbose_name='Страна')

    def __str__(self):
        return self.title

class Artist(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    info = models.TextField(verbose_name='Информация', blank=True, null=True)
    foto = models.FileField(verbose_name='Фото', upload_to='artist/', null=True, blank=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    info = models.TextField(verbose_name='Информация', blank=True, null=True)
    foto = models.FileField(verbose_name='Фото', upload_to='director/', null=True, blank=True)

    def __str__(self):
        return self.name

class Podpiska(models.Model):
    title = models.CharField(max_length=100, verbose_name='Подписка')
    price = models.IntegerField(verbose_name='Стоимость')

    def __str__(self):
        return self.title

class Kino(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    genre = models.ManyToManyField(Genre)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True,verbose_name='Страна')
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True,verbose_name='Режиссер')
    artist = models.ManyToManyField(Artist)
    info = models.TextField( verbose_name='Информация', blank=True, null=True)
    year = models.IntegerField(verbose_name='Год')
    poster = models.FileField(verbose_name='Постер', upload_to='posters/', null=True, blank=True)
    rating = models.FloatField(blank=True, null=True,verbose_name='Рейтинг')
    trailer = models.URLField(blank=True, null=True,verbose_name='Ссылка')
    podpiska = models.ForeignKey(Podpiska, on_delete=models.SET_NULL, null=True, blank=True,verbose_name='Подписка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'{self.title}/{str(self.id)}/'