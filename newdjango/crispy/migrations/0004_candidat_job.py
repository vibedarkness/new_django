# Generated by Django 4.0.6 on 2022-09-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crispy', '0003_candidat_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidat',
            name='job',
            field=models.CharField(default='', max_length=5),
        ),
    ]
