# Generated by Django 3.2 on 2021-12-28 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0013_auto_20211224_1541'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(help_text='message', max_length=500, verbose_name='message')),
                ('apply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.apply', verbose_name='apply')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='message.message', verbose_name='reponses')),
            ],
            options={
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['id'], name='message_mes_id_f4899c_idx'),
        ),
    ]