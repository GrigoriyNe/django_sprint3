from django.db import models
from django.contrib.auth import get_user_model
from core.models import PublishedModel
from django.db.models.query import QuerySet
from django.utils import timezone


now = timezone.now()
User = get_user_model()


class PostQuerySet(models.query.QuerySet):
    def published(self):
        return self.filter(
            is_published=True,
            pub_date__lt=now,
            category__is_published=True)


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


class Post(PublishedModel):
    title = models.CharField(
        'Заголовок',
        blank=False,
        max_length=256,
    )
    text = models.TextField(
        'Текст',
        blank=False,
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        blank=False,
        help_text='Если установить дату и время '
        'в будущем — можно делать '
        'отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
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
        blank=False,
        related_name='category',
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True,
    )
   # PublishedPostManager = PostQueryset.as_manager
    objects = PostQuerySet.as_manager()
  #  published = PublishedPostManager()
    published = PostQuerySet.as_manager()

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
