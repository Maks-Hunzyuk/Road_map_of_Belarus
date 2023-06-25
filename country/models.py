from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Region(models.Model):
    """Регионы"""
    title = models.CharField(max_length=100, verbose_name="Регионы")

    def __str__(self):
        return self.title


class Cities(models.Model):
    """список городов в регионе"""

    title = models.CharField(max_length=100, verbose_name="Название города")
    discription = models.TextField(verbose_name="Описание")
    short_discription = models.CharField(max_length=255, blank=True, verbose_name="Краткое описание")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_7 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_8 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_9 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_10 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_11 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_12 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_13 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_14 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_15 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_16= models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_17 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_18 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_19 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    photo_20 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото")
    region = models.ForeignKey("Region", on_delete=models.CASCADE, verbose_name="Регионы")

    def __str__(self):
        return self.title


class Transport(models.Model):
    "Описание городского транспорта"

    discription = models.TextField(verbose_name="описание")
    link_1 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_2 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_3 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_4 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_5 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_6 = models.URLField(blank=True, verbose_name="ссылка на источник")
    city = models.ForeignKey("Cities", on_delete=models.CASCADE, verbose_name='Город')

    def __str__(self):
        return self.discription


class Hotels(models.Model):
    """Отели в городе"""

    title = models.CharField(max_length=100, verbose_name="Название отеля")
    discription = models.TextField(verbose_name="описание")
    link_1 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_2 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_3 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_4 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_5 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_6 = models.URLField(blank=True, verbose_name="ссылка на источник")
    city = models.ForeignKey("Cities", on_delete=models.CASCADE, verbose_name='Город')

    
    def __str__(self):
        return self.discription



class CulturalObjects(models.Model):
    """Культурные обьекты в городе"""

    title = models.CharField(max_length=100, blank=True, verbose_name="Название")
    discription = models.TextField(verbose_name="описание")
    link_1 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_2 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_3 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_4 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_5 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_6 = models.URLField(blank=True, verbose_name="ссылка на источник")
    photo_1 = models.ImageField(upload_to='cultural_objects/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_2 = models.ImageField(upload_to='cultural_objects/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_3 = models.ImageField(upload_to='cultural_objects/%Y/%m/%d/', blank=True, verbose_name='Фото')
    city = models.ForeignKey("Cities", on_delete=models.CASCADE, verbose_name='Город')

    def __str__(self):
        return self.title

    
class Food(models.Model):
    """Заведения общепита в городе"""

    title = models.CharField(max_length=100, verbose_name="Название")
    discription = models.TextField(verbose_name="описание")
    link_1 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_2 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_3 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_4 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_5 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_6 = models.URLField(blank=True, verbose_name="ссылка на источник")
    city = models.ForeignKey("Cities", on_delete=models.CASCADE, verbose_name='Город')

    def __str__(self):
        return self.title


class Shopping(models.Model):
    """Магазины города"""

    title = models.CharField(max_length=100, verbose_name="Название")
    discription = models.TextField(verbose_name="описание")
    link_1 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_2 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_3 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_4 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_5 = models.URLField(blank=True, verbose_name="ссылка на источник")
    link_6 = models.URLField(blank=True, verbose_name="ссылка на источник")
    city = models.ForeignKey("Cities", on_delete=models.CASCADE, verbose_name='Город')

    def __str__(self):
        return self.title
    

class Routers(models.Model):
    """список всех марщрутов"""

    title = models.CharField(max_length=255, verbose_name='Название маршрута')
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    description =  models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos_routers/%Y/%m/%d/', verbose_name='Фото')


    def __str__(self):
        return self.title


class RouteDetails(models.Model):
    """Детали маршрутов"""

    title = models.CharField(max_length=255, verbose_name='Путкты остановки')
    stopping_points_desc = models.TextField(verbose_name='Описания города')
    photo_1 = models.ImageField(upload_to='photos_route_details/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_2 = models.ImageField(upload_to='photos_route_details/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_3 = models.ImageField(upload_to='photos_route_details/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_1 = models.ImageField(upload_to='photos_route_details/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_2 = models.ImageField(upload_to='photos_route_details/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_3 = models.ImageField(upload_to='photos_route_details/%Y/%m/%d/', blank=True, verbose_name='Фото')
    router = models.ForeignKey('Routers', on_delete=models.CASCADE, verbose_name='Маршруты',related_name='routers')

    def __str__(self):
        return self.title
    

class Events(models.Model):
    """Список событий кино выставки и тд"""

    title = models.CharField(max_length=255, verbose_name='Название подборки')
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    photo = models.ImageField(upload_to='events_photo/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title



class Events_ditails(models.Model):
    """Детали событий кино выставки и тд"""
    
    title = models.CharField(max_length=255, verbose_name='Название')
    where = models.CharField(max_length=255, verbose_name='Место проведения', blank=True)
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='events_photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    date = models.TextField(verbose_name='Дата проведения события')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Стоймость')
    link = models.URLField(blank=True, verbose_name='Ссылка на источник')
    event = models.ForeignKey('Events', on_delete=models.CASCADE, verbose_name='События', related_name='events')

    def __str__(self):
        return self.title
    

class Photos(models.Model):
    """Посты с фотографиями"""

    title = models.CharField(max_length=255, verbose_name='Название подборки')
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    photo = models.ImageField(upload_to='events_photo/%Y/%m/%d/', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.title

class PhotosDiscriptions(models.Model):
    """Детали фотографий"""

    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name="Описание")
    photo_1 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_2 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_3 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_4 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_5 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_6 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_7 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_8 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    photo_9 = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    external_key = models.ForeignKey("Photos", on_delete=models.CASCADE, verbose_name='Рубрика фотографий', related_name='photos')



class Comment(models.Model):
    name = models.CharField(max_length=80, verbose_name="Автор")
    body = models.TextField(verbose_name="Текст комментария")
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')
    active = models.BooleanField(default=True, db_index=True, verbose_name='Выводить на экран?')

    class Meta:
        verbose_name_plural = "Комментарии"
        verbose_name = "Комментарий"
        ordering = ('created',)
        