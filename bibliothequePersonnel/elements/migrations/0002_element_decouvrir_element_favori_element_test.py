# Generated by Django 4.0.4 on 2022-06-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='decouvrir',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='element',
            name='favori',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='element',
            name='test',
            field=models.IntegerField(default=0),
        ),
    ]