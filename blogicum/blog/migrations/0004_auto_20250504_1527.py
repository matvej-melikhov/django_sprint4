# Generated by Django 3.2.16 on 2025-05-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20250504_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Добавлено'),
        ),
    ]
