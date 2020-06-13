# Generated by Django 3.0.3 on 2020-06-13 17:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tour_store', '0010_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact',
            new_name='message',
        ),
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=40),
            preserve_default=False,
        ),
    ]
