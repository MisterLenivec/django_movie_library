# Generated by Django 3.0.6 on 2020-05-29 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200507_1304'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstar',
            options={'ordering': ['-value'], 'verbose_name': 'Звезда рейтинга', 'verbose_name_plural': 'Звёзды рейтинга'},
        ),
    ]
