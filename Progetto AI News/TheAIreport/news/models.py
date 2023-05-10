from django.db import models

# Create your models here.
class News(models.Model):
    link = models.CharField(("link"), max_length = 300)
    titolo = models.CharField(("titolo"),max_length = 300)
    contenuto = models.CharField(("contenuto"),max_length = 700)
    data = models.CharField(("data"),max_length = 40)