# Generated by Django 4.1 on 2022-08-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='signature',
            field=models.CharField(default='Firma', max_length=100),
        ),
    ]
