# Generated by Django 4.2.6 on 2023-10-18 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolstoreapp', '0003_course_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=200)),
                ('bimg', models.ImageField(upload_to='pics')),
                ('bdesc', models.TextField()),
            ],
        ),
    ]