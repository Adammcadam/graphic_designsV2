# Generated by Django 3.0.2 on 2020-06-27 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200627_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
    ]
