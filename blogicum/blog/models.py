from django.db import models
from django.contrib.auth import get_user_model
from core.models import PublishedModel

User = get_user_model()


class Category(PublishedModel):
    title = models.CharField('Заголовок', blank=False, max_length=256)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор', max_length=64, unique=True,
                            help_text='Идентификатор страницы для URL; '
                            'разрешены символы латиницы, цифры, дефис '
                            'и подчёркивание.'
                            )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(PublishedModel):
    name = models.CharField('Название места', max_length=256)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(PublishedModel):
    title = models.CharField('Заголовок', blank=False, max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата и время публикации',
                                    help_text='Если установить дату и время '
                                    'в будущем — можно делать '
                                    'отложенные публикации.'
                                    )
    author = models.ForeignKey(
        User,
        blank=False,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE
    )

    location = models.ForeignKey(
        Location,
        blank=True,
        verbose_name='Местоположение',
        default='null',
        related_name='location',
        on_delete=models.SET_NULL, null=True
    )

    category = models.ForeignKey(
        Category,
        blank=False,
        related_name='category',
        verbose_name='Категория',
        on_delete=models.SET_NULL, null=True
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
