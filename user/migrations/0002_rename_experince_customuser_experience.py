# Generated by Django 3.2.9 on 2021-12-10 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='experince',
            new_name='experience',
        ),
    ]
