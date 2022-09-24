# Generated by Django 4.1.1 on 2022-09-11 19:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['date_of_publication']},
        ),
        migrations.RemoveField(
            model_name='photo',
            name='date_time_of_publication',
        ),
        migrations.AddField(
            model_name='photo',
            name='date_of_publication',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(max_length=300, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo_file',
            field=models.ImageField(upload_to='images/', verbose_name='Pet Photo'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='tagged_pets',
            field=models.ManyToManyField(to='pets.pet', verbose_name='Tag Pets'),
        ),
    ]