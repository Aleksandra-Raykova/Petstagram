# Generated by Django 4.1.1 on 2022-09-15 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_first_name_alter_profile_last_name'),
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]