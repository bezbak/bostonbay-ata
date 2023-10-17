# Generated by Django 4.2.5 on 2023-09-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ADS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_ads', models.ImageField(upload_to='ads/', verbose_name='Фото верхней рекламы')),
                ('top_ads_link', models.URLField(verbose_name='Ссылка верхней рекламы')),
                ('cat_ads', models.ImageField(upload_to='ads/', verbose_name='Фото рекламы в меню')),
                ('cat_ads_link', models.URLField(verbose_name='Ссылка рекламы в меню')),
            ],
            options={
                'verbose_name': 'Реклама',
                'verbose_name_plural': 'Реклама',
            },
        ),
    ]