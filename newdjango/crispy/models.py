from email import message
from django.db import models


class Candidat(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.CharField(max_length=3, default="")
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=25,default="")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname
