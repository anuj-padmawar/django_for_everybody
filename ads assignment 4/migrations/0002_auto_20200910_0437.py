# Generated by Django 3.1 on 2020-09-10 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='favorites',
        ),
        migrations.DeleteModel(
            name='Fav',
        ),
    ]