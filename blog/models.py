from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Tag(models.Model):
    text = models.CharField(max_length=20)

    def __str__(self):
        return self.text

class Post(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    main_image = models.ImageField(upload_to="posts", null=True, blank=True)
    image_caption = models.CharField(max_length=100, null=True,blank=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title