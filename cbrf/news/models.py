from django.db import models
from companies.models import Organisation


class NewsCategories(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Наименование категории новостей'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Наименование тега новостей'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Тег новости"
        verbose_name_plural = "Теги новости"

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок новости'
    )
    text = models.TextField(
        verbose_name='Текст новости'
    )
    category_id = models.ForeignKey(
        NewsCategories,
        on_delete=models.CASCADE,
        verbose_name='Новостная категория'
    )
    image = models.ImageField(
        verbose_name='Изображение к новости',
        upload_to='news_images/',
        null=True,
        blank=True
    )
    date = models.DateField(
        verbose_name='Дата'
    )
    class Meta:
        ordering = ["date"]
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class News_Tags(models.Model):
    news_id = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
    )
    tags_id = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE
    )

class Feedback(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronimic_name = models.CharField(max_length=100)
    contract_number = models.CharField(max_length=50)
    contract_date = models.DateField()
    message = models.TextField()
    organization = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    send_to_email = models.BooleanField(default=False)

    def __str__(self):
        return f"Обратная связь по организации {self.organization}"