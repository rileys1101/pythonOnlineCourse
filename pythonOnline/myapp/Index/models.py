from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=225)
    def __str__(self):
        return str(self.title)

class UserForm(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.name