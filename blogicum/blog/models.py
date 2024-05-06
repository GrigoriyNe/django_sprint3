from core.models import PublishedModel

from django.contrib.auth import get_user_model

from django.db import models

from django.utils import timezone


now = timezone.now()
User = get_user_model()


class Category(PublishedModel):
    title = models.CharField(
        'Заголовок',
        max_length=256,
        blank=False,
    )
    description = models.TextField(
        'Описание',
        blank=False,
    )
    slug = models.SlugField(
        'Идентификатор',
        max_length=64,
        unique=True,
        blank=False,
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
    name = models.CharField(
        'Название места',
        max_length=256,
        blank=False,
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(
            is_published=True,
            pub_date__lt=now,
            category__is_published=True)


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model)

    def published(self):
        return self.get_queryset().published()


class Post(PublishedModel):

    objects = models.Manager()

    published = PublishedPostManager()

    title = models.CharField(
        'Заголовок',
        max_length=256,
    )
    text = models.TextField(
        'Текст',
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text='Если установить дату и время '
        'в будущем — можно делать '
        'отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',
    )

    location = models.ForeignKey(
        Location,
        blank=True,
        verbose_name='Местоположение',
        related_name='location',
        on_delete=models.SET_NULL,
        null=True,
    )

    category = models.ForeignKey(
        Category,
        related_name='posts',
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
