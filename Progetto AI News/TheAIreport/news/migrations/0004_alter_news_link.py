# Generated by Django 4.2 on 2023-05-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_link_alter_news_titolo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(max_length=200, null=True),
        ),
    ]