# Generated by Django 3.2.9 on 2021-12-16 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20211213_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(choices=[('Digital', 'Digital & Creative'), ('Sales', 'Sales & Marketing'), ('Marketing', 'Marketing & PR'), ('Contractor', 'IT Contractor'), ('Others', 'Others Job')], max_length=10, verbose_name='category title'),
        ),
    ]
