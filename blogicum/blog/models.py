from django.db import models
from django.contrib.auth import get_user_model
from core.models import PublishedModel
User = get_user_model()

class Category(PublishedModel):
    title = models.CharField('Заголовок', max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор', max_length=64)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title



class Location(PublishedModel):
    name = models.TextField('Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(PublishedModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата и время публикации')
    
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    location = models.ForeignKey(
        Location,
        default='Планета Земля',
        related_name='location',
        on_delete=models.SET_NULL, null=True
    )

    category = models.ForeignKey(
        Category,
        related_name='category',
        on_delete=models.SET_NULL, null=True
    )

    

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
