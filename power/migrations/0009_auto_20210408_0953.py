# Generated by Django 3.1.2 on 2021-04-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('power', '0008_vacancyform_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancyform',
            name='citizenship',
            field=models.ImageField(null=True, upload_to='static/usercitizen'),
        ),
        migrations.AlterField(
            model_name='vacancyform',
            name='cv',
            field=models.FileField(null=True, upload_to='static/useruploads'),
        ),
    ]
