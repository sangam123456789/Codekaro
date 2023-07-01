# Generated by Django 3.2.19 on 2023-07-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_recursion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beginner',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='binary',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='brain',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='brute',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='dp',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='dpstand',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='dsu',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='graph',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='greed',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='hash',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='implement',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='pair',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='pointer',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='recursion',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='segtree',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='sort',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='sub',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
        migrations.AlterField(
            model_name='tree',
            name='description',
            field=models.TextField(default='Do it yourself!', max_length=150),
        ),
    ]
