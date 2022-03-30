from os import link
from django.db import models
from django.urls import reverse

class Source(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    history = models.TextField()
    hyperlink = models.URLField()

    def __str__(self):
        name = f"{self.first_name} {self.last_name}"
        return name
class Quote(models.Model):
    text = models.TextField(max_length=1000)
    source = models.ManyToManyField(Source)
    
    def __str__(self):
        list = self.text.split()[:10] + '...'
        newStr = ' '.join(list)
        return newStr
    