from django.db import models


class ProductClass(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название типа продукта'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"

    def __str__(self):
        return self.name


class OrganisationType(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название типа организации'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название типа продукта'
    )
    organisation_type_id = models.ForeignKey(
        OrganisationType,
        on_delete=models.CASCADE,
        verbose_name='Тип организации'
    )
    product_class_id = models.ForeignKey(
        ProductClass,
        on_delete=models.CASCADE,
        verbose_name='Класс продукта'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Тип продукта"
        verbose_name_plural = "Типы продуктов"

    def __str__(self):
        return self.name


class Organisation(models.Model):
    name_short = models.CharField(
        max_length=50,
        verbose_name="Короткое наименование компании"
    )
    name_long = models.CharField(
        max_length=500,
        verbose_name="Полное наименование компании"
    )
    brand_name = models.CharField(
        max_length=250,
        verbose_name="Бренд"
    )
    inn = models.IntegerField(
        verbose_name="ИНН"
    )
    ogrn = models.IntegerField(
        verbose_name="ОГРН"
    )
    location_reg = models.CharField(
        max_length=550,
        verbose_name='Местонахождение'
    )
    date_reg = models.DateField(
        verbose_name='Дата регистрации'
    )
    organisation_type_id = models.ForeignKey(
        OrganisationType,
        on_delete=models.CASCADE,
        verbose_name='Тип организации'
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.name_short


class Region(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Город'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class City(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Город'
    )
    region_id = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        verbose_name='Регион'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Filial(models.Model):
    organisation_id = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        verbose_name='Организация'
    )
    location_fact = models.CharField(
        max_length=500,
        verbose_name="Местонахождение филиала"
    )
    email = models.EmailField(
        verbose_name="Е-мейл"
    )
    schedule = models.JSONField(
        verbose_name="Расписание"
    )
    phone = models.IntegerField(
        verbose_name="Номер телефона"
    )
    city_id = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='Город'
    )

    class Meta:
        ordering = ["organisation_id"]
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"


class Product(models.Model):
    filial_id = models.ForeignKey(
        Filial,
        on_delete=models.CASCADE,
        verbose_name='Филиал организации'
    )
    name = models.CharField(
        max_length=500,
        verbose_name="Название продукта"
    )
    product_type_id = models.ForeignKey(
        ProductType,
        on_delete=models.CASCADE,
        verbose_name='Тип продукта'
    )
    params = models.CharField(
        max_length=250,
        verbose_name="Другие параметры"
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
