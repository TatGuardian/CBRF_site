# Generated by Django 4.2.9 on 2024-04-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_heading_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cbrf/news_images/', verbose_name='Изображение к новости'),
        ),
    ]