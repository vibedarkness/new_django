from email import message
from django.db import models

statuschoice=(
    ('Attente','Attente'),
    ('Approuver','Approuver'),
    ('Desapprouver','Desapprouver')
)

class Candidat(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    age = models.CharField(max_length=3, default="")
    job=models.CharField(max_length=5, default="")
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=25,default="")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,null=True,choices=statuschoice, default="Attente")


    def clean(self):
        self.firstname=self.firstname.capitalize()
        self.lastname=self.lastname.capitalize()

    def __str__(self):
        return self.firstname
