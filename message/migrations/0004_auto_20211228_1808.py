# Generated by Django 3.2 on 2021-12-28 18:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_auto_20211228_1758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'get_latest_by': ['created'], 'ordering': ['created'], 'verbose_name_plural': 'chats'},
        ),
        migrations.AddField(
            model_name='chat',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddIndex(
            model_name='chat',
            index=models.Index(fields=['id'], name='message_cha_id_7af706_idx'),
        ),
    ]