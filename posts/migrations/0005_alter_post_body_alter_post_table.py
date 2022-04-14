# Generated by Django 4.0.3 on 2022-04-06 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(db_index=True, max_length=140, null=True, verbose_name='Body'),
        ),
        migrations.AlterModelTable(
            name='post',
            table='posts',
        ),
    ]
