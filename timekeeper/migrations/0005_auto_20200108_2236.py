# Generated by Django 3.0 on 2020-01-08 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timekeeper', '0004_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
    ]
