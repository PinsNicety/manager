# Generated by Django 2.2.7 on 2020-03-03 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walktest', '0002_remove_walktest_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='walktest',
            name='site',
            field=models.CharField(choices=[('Sci-Tech', 'Sci-Tech'), ('Bowels', 'Bowels'), ('Wilbraham Middle School', 'Wilbraham Middle School')], default=None, max_length=200),
            preserve_default=False,
        ),
    ]
