# Generated by Django 2.0.4 on 2018-04-17 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alize', '0004_category_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('img', models.CharField(max_length=100, null=True, verbose_name='Фото')),
            ],
        ),
    ]
