from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from cbrf.settings import COMPANY_TYPES  # Допилить типы
from django.contrib.auth import get_user_model


User = get_user_model()


class Company(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование компании",
        help_text="Введите наименование",
    )
    description = models.TextField(
        max_length=1000,
        verbose_name="Описание компании",
        help_text="Введите описание"
    )
    typ = models.CharField(
        max_length=255,
        verbose_name="Наименование типа",
        help_text="Выберите тип",
        null=False,
        blank=False,
        choices=COMPANY_TYPES
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        on_delete=models.CASCADE
    )
    image = ProcessedImageField(
        upload_to="product_images/",
        verbose_name="Основное изображение",
        help_text="Загрузите изображение",
    )
    big_image = ImageSpecField(
        source="image",
        processors=[ResizeToFill(1000, 1000)],
        format="JPEG",
        options={"quality": 100},
    )
    preview_image = ImageSpecField(
        source="image",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 80},
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return self.name
