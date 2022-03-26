
from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    facebook_url = models.URLField(max_length=255)
    twitter_url = models.URLField(max_length=255)
    google_plus_url = models.URLField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name