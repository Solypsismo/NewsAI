# Generated by Django 4.2 on 2023-05-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_news_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='immagine',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
