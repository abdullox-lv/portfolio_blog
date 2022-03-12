from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField("Category", max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField("Title", max_length=150)
    summary = models.CharField("Summary", max_length=150)
    body = models.TextField("Text")
    photo = models.ImageField('Image', upload_to='post_images/')


    def __str__(self):
        return self.title
