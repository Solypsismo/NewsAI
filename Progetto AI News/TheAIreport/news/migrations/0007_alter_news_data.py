# Generated by Django 4.2 on 2023-05-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_remove_news_immagine_alter_news_contenuto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='data',
            field=models.CharField(max_length=40),
        ),
    ]
