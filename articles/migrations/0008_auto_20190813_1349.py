# Generated by Django 2.1.4 on 2019-08-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20190807_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]