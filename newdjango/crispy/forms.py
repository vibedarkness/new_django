from django import forms
from django.core.validators import RegexValidator
from .models import Candidat

# Gestion du lowercase


class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()

# Gestion du Uppercase


class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class CandidatForm(forms.ModelForm):

    # validations
    firstname = forms.CharField(label='Prenom', min_length=3, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9]*$', message='ce champ ne dois contenir que des lettres')], widget=forms.TextInput(attrs={'placeholder': 'Prenom'}))
    lastname = forms.CharField(label='Nom', min_length=2, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9]*$', message='ce champ ne dois contenir que des lettres')], widget=forms.TextInput(attrs={'placeholder': 'Nom'}))
    age = forms.CharField(label='Age', min_length=1, max_length=3, validators=[RegexValidator(
        r'^[0-9]*$', message='ce champ ne dois contenir que des entiers')], widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    email = Lowercase(label='Email', min_length=5, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message="ceci n'est pas un email valide")], widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    # phone = forms.CharField(label='Telephone' ,min_length=1, max_length=3, validators=[RegexValidator(r'^[0-9]*$', message='ce champ ne dois contenir que des entiers')], widget=forms.TextInput(attrs= {'placeholder':'Telephone'}))
    message = Lowercase(label='Message', required=True, min_length=10, max_length=1000,
                              widget=forms.Textarea(attrs={'placeholder': 'Messages', 'rows': 4}))

    experience=forms.BooleanField(label='Avez vous un experience professionnelle', required=False)


    job = Uppercase(
        label='Fonction',
        min_length=5,
        max_length=5,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex:FR-22',
        })

    )
    # GENRE=[('M','Masculin'),('F','Feminin')]
    # genre=forms.CharField(label='Genre',widget=forms.RadioSelect(choices=GENRE))

    class Meta:
        model = Candidat
        # fields = ['firstname', 'lastname','job', 'email', 'age', 'phone', 'message']
        exclude = ['created_at', 'status']

        SALAIRE = (
            ('', 'Choisissez votre attente salairial par mois'),
            ('entre (100000 Fcfa et 200000)', 'entre (100000 Fcfa et 200000)'),
            ('entre (200000 Fcfa et 300000)', 'entre (200000 Fcfa et 300000)'),
            ('entre (300000 Fcfa et 500000)', 'entre (300000 Fcfa et 500000)'),
            ('entre (500000 Fcfa et 1000000)', 'entre (500000 Fcfa et 1000000)')
        )
        GENRE = [('M', 'Masculin'), ('F', 'Feminin')]
        FUMEUR = (
            ('1', 'Oui'),
            ('2', 'Non')

        )

        widgets = {
            'phone': forms.TextInput(attrs={
                'style': 'font-size: 15px',
                'placeholder': 'Telephone',
                'data-mask': '(+000) 00-000-00-00'
            }),

            'salaire': forms.Select(
                choices=SALAIRE,
                attrs={
                    'class': 'form-control',
                }),
            'genre': forms.RadioSelect(choices=GENRE, attrs={'class': 'btn-check'}),
            'fumeur': forms.RadioSelect(choices=FUMEUR, attrs={'class': 'btn-check'})

        }
