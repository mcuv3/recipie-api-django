# Generated by Django 3.1.1 on 2020-09-04 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logout',
            field=models.BooleanField(default=True),
        ),
    ]
