# Generated by Django 4.2 on 2023-05-29 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_category_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
    ]
