# Generated by Django 3.2.19 on 2023-06-30 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brain',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
