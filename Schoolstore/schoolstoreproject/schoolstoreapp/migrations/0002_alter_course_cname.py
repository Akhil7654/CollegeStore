# Generated by Django 4.2.6 on 2023-10-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolstoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='cname',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
