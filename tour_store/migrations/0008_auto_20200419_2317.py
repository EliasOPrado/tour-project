# Generated by Django 3.0.3 on 2020-04-19 23:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour_store', '0007_auto_20200323_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinations',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]