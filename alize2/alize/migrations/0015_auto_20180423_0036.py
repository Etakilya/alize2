# Generated by Django 2.0.4 on 2018-04-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alize', '0014_auto_20180422_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(default='Write your Comment', verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date'),
        ),
    ]
