# Generated by Django 4.0.2 on 2022-03-26 15:10

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
