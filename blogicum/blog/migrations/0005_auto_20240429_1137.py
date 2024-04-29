# Generated by Django 3.2.16 on 2024-04-29 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20240429_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='id_pole',
            field=models.IntegerField(default=2, verbose_name='id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='id_pole',
            field=models.IntegerField(default=1, verbose_name='id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='id_pole',
            field=models.IntegerField(default=3, verbose_name='id'),
            preserve_default=False,
        ),
    ]
