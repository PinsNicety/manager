# Generated by Django 3.0.2 on 2020-03-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walktest', '0007_auto_20200307_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='walktest',
            name='time',
            field=models.DateTimeField(default=None),
        ),
    ]