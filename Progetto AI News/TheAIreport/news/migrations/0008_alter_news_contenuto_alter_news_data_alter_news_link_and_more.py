# Generated by Django 4.2 on 2023-05-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_news_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='contenuto',
            field=models.CharField(max_length=700, verbose_name='contenuto'),
        ),
        migrations.AlterField(
            model_name='news',
            name='data',
            field=models.CharField(max_length=40, verbose_name='data'),
        ),
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(max_length=300, verbose_name='link'),
        ),
        migrations.AlterField(
            model_name='news',
            name='titolo',
            field=models.CharField(max_length=300, verbose_name='titolo'),
        ),
    ]