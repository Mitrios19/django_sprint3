# Generated by Django 3.2.16 on 2024-12-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=111, unique=True, verbose_name='Слаг'),
            preserve_default=False,
        ),
    ]
