from tkinter.ttk import Style
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
        r'^[a-zA-Z0-9]*$', message='ce champ ne dois contenir que des lettres')], widget=forms.TextInput(attrs={'placeholder': 'Prenom', 'style': 'font-size:13px; text-transform: capitalize'}))
    lastname = forms.CharField(label='Nom', min_length=2, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9]*$', message='ce champ ne dois contenir que des lettres')], widget=forms.TextInput(attrs={'placeholder': 'Nom', 'style': 'font-size:13px; text-transform: capitalize'}))
    age = forms.CharField(label='Age', min_length=1, max_length=3, validators=[RegexValidator(
        r'^[0-9]*$', message='ce champ ne dois contenir que des entiers')], widget=forms.TextInput(attrs={'placeholder': 'Age','style':'font-size:13px'}))
    email = Lowercase(label='Email', min_length=5, max_length=50, validators=[RegexValidator(
        r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message="ceci n'est pas un email valide")], widget=forms.TextInput(attrs={'placeholder': 'Email','style':'font-size:13px'}))
    # phone = forms.CharField(label='Telephone' ,min_length=1, max_length=3, validators=[RegexValidator(r'^[0-9]*$', message='ce champ ne dois contenir que des entiers')], widget=forms.TextInput(attrs= {'placeholder':'Telephone'}))
    message = Lowercase(label='Message', required=False, min_length=10, max_length=1000,
                              widget=forms.Textarea(attrs={'placeholder': 'Messages', 'rows': 2}))

    fichier=forms.FileField(label='Entrez votre cv', widget=forms.ClearableFileInput(attrs={'style':'font-size:13px'}))

    experience = forms.BooleanField(
        label='Avez vous un experience professionnelle?', required=False)

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

        labels = {
            'fumeur': 'Vous fumer?',
        }

        widgets = {
            'phone': forms.TextInput(attrs={
                'style': 'font-size: 13px',
                'placeholder': 'Telephone',
                'data-mask': '(+000) 00-000-00-00'
            }),

            'salaire': forms.Select(
                choices=SALAIRE,
                attrs={
                    'class': 'form-control',
                    'style':'font-size:13px',
                }),
            'genre': forms.RadioSelect(choices=GENRE, attrs={'class': 'btn-check'}),
            'fumeur': forms.RadioSelect(choices=FUMEUR, attrs={'class': 'btn-check'}),
            'personnality':forms.Select(attrs={'style':'font-size:13px;'})

        }

    # super fonction
    def __init__(self, *args, **kwargs):
        super(CandidatForm, self).__init__(*args, **kwargs)

        # control panel
        # input required
        self.fields["message"].required = True

        # input desactivé
        # self.fields["firstname"].disabled=True

        # input readonly
        # self.fields["email"].widget.attrs.update({'readonly':'readonly'})

        # readonly for full input(meme chose pour disabled(desactivé))

        # readonly=["firstname","lastname","age","email","phone","message"]

        # for readvibe in readonly:
        #     self.fields[readvibe].widget.attrs['readonly']='true'

        # select option
        self.fields["personnality"].choices = [
            ('', 'Choisissez votre personnalité'), ] + list(self.fields["personnality"].choices)[1:]
