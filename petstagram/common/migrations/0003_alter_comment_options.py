# Generated by Django 4.1.1 on 2022-09-29 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on']},
        ),
    ]
