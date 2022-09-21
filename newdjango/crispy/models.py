from email import message
from django.db import models

statuschoice=(
    ('Attente','Attente'),
    ('Approuver','Approuver'),
    ('Desapprouver','Desapprouver')
)

PERSONNALITY=(
    ('','Choisissez votre personnalité'),
    ('Je suis agile','Je suis agile'),
    ('Je suis ambitieux','Je suis ambitieux'),
    ('Je suis sournois','Je suis sournois'),
    ('Je suis pathetique','Je suis pathetique'),
    ('Je suis absentheiste','Je suis absentheiste')
)

FUMEUR=(
    ('1','Oui'),
    ('2','Non')

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
    personnality=models.CharField(max_length=200, null=True ,choices=PERSONNALITY)
    salaire=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    experience=models.BooleanField(null=True)
    fumeur=models.CharField(max_length=200, default="",choices=FUMEUR)



    def clean(self):
        self.firstname=self.firstname.capitalize()
        self.lastname=self.lastname.capitalize()

    def __str__(self):
        return self.firstname
