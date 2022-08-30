# Generated by Django 3.2.9 on 2021-12-10 10:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'is_company': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'user__is_job_seeker': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='job seeker'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_active': True, 'user__is_job_seeker': True}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='job seeker'),
        ),
        migrations.AddField(
            model_name='apply',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='apply',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.offer'),
        ),
    ]
