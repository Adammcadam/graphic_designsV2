# Generated by Django 3.0.2 on 2020-06-22 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200622_1758'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='finish',
        ),
    ]
