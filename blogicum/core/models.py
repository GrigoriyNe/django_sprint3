from django.db import models


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано',
        blank=False,
        default=True,
        help_text='Снимите '
        'галочку, чтобы скрыть публикацию.'
        )
    created_at = models.DateTimeField(
        'Добавлено',
        blank=False,
        auto_now_add=True,
        )

    class Meta:
        abstract = True
