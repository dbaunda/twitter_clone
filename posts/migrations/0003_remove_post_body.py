# Generated by Django 4.0.3 on 2022-04-05 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
    ]
