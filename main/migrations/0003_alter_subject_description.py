# Generated by Django 4.2 on 2023-05-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(),
        ),
    ]