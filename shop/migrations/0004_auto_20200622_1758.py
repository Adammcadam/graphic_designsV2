# Generated by Django 3.0.2 on 2020-06-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_finish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='finish',
            field=models.CharField(choices=[('G', 'Gloss'), ('M', 'Matte')], default='Gloss', max_length=254),
        ),
    ]
