from django.db import models
from django.contrib.auth.models import User


# ebook model
class Ebook(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=255)
    pages = models.IntegerField()
    price = models.FloatField()
    # this will be the download link of the ebook and image
    image = models.FileField(upload_to='media/images/')
    ebook = models.FileField(upload_to='media/ebooks/')
    user= models.ForeignKey(User ,null=True,  on_delete=models.CASCADE )


    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField()
    pub_time = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE)

    def __str__(self):
        return self.body








































# category model
class Category(models.Model):

    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

