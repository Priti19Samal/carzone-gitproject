# Generated by Django 4.1.4 on 2022-12-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='photo',
            field=models.ImageField(upload_to='photos/%y/%m/%d/'),
        ),
    ]
