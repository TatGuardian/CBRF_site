# Generated by Django 4.2.9 on 2024-04-27 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_region_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='name_long',
            new_name='name_full',
        ),
        migrations.RemoveField(
            model_name='product',
            name='params',
        ),
        migrations.AddField(
            model_name='organisation',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта организации'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Телефон организации'),
        ),
        migrations.AddField(
            model_name='product',
            name='age_min',
            field=models.IntegerField(blank=True, default=18, verbose_name='Минимальный возраст'),
        ),
        migrations.AddField(
            model_name='product',
            name='amount_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Максимальная сумма предложения'),
        ),
        migrations.AddField(
            model_name='product',
            name='amount_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Минимальная сумма предложения'),
        ),
        migrations.AddField(
            model_name='product',
            name='frequency_payment',
            field=models.CharField(blank=True, choices=[('monthly', 'Ежемесячно'), ('annually', 'Ежегодно'), ('quater', 'Ежеквартально'), ('end', 'В конце срока'), ('other', 'Иное')], max_length=20, null=True, verbose_name='Частота выплат'),
        ),
        migrations.AddField(
            model_name='product',
            name='insurance',
            field=models.BooleanField(blank=True, null=True, verbose_name='Наличие или отсутствие страхования'),
        ),
        migrations.AddField(
            model_name='product',
            name='interest_payment',
            field=models.FloatField(blank=True, null=True, verbose_name='Сумма, которую составит регулярная выплата процентов'),
        ),
        migrations.AddField(
            model_name='product',
            name='method_reg',
            field=models.CharField(choices=[('Online', 'Онлайн'), ('Offline', 'Офлайн')], default='Offline', max_length=20, verbose_name='Метод оформления'),
        ),
        migrations.AddField(
            model_name='product',
            name='purpose',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Цель'),
        ),
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Ставка процента'),
        ),
        migrations.AddField(
            model_name='product',
            name='term',
            field=models.IntegerField(blank=True, null=True, verbose_name='Срок в днях'),
        ),
        migrations.AlterField(
            model_name='filial',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта филиала'),
        ),
        migrations.AlterField(
            model_name='filial',
            name='phone',
            field=models.IntegerField(verbose_name='Номер телефона филиала'),
        ),
        migrations.AlterField(
            model_name='filial',
            name='schedule',
            field=models.JSONField(verbose_name='Расписание филиала'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='name_short',
            field=models.CharField(max_length=50, verbose_name='Краткое наименование компании'),
        ),
    ]