# Generated by Django 3.0 on 2020-03-15 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walktest', '0009_auto_20200307_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walktest',
            name='site_name',
            field=models.CharField(choices=[('Riverview', 'Riverview'), ('Mile Tree', 'Mile Tree'), ('Sullivan Housing', 'Sullivan Housing'), ('Towers', 'Towers'), ('Minnechaug', 'Minnechaug')], max_length=200),
        ),
    ]
