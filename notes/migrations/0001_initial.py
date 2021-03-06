# Generated by Django 3.0.2 on 2020-02-18 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('street_address', models.CharField(default=None, max_length=50)),
                ('city', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('zip_code', models.IntegerField(default=None)),
                ('contact_name', models.CharField(default=None, max_length=50)),
                ('area_code', models.SmallIntegerField(default=None)),
                ('prefix', models.SmallIntegerField(default=None)),
                ('line_number', models.SmallIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('street_address', models.CharField(default=None, max_length=50)),
                ('city', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('zip_code', models.IntegerField(default=None)),
                ('contact_name', models.CharField(default=None, max_length=50)),
                ('area_code', models.SmallIntegerField(default=None)),
                ('prefix', models.SmallIntegerField(default=None)),
                ('line_number', models.SmallIntegerField(default=None)),
                ('organization', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='notes.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('body', djrichtextfield.models.RichTextField()),
                ('site', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='notes.Site')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
