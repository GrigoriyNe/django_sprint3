from django.db import models


class PublishedModel(models.Model):
    is_published = models.BooleanField('Опубликовано', default=True)
    created_at = models.DateTimeField('Добавлено')
                                      
    class Meta:
        abstract = True
