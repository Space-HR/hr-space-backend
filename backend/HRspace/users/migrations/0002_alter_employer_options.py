# Generated by Django 4.2.9 on 2024-03-19 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employer',
            options={'verbose_name': 'Работодатель', 'verbose_name_plural': 'Работодатели'},
        ),
    ]
