# Generated by Django 5.1.1 on 2025-03-21 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='event',
        ),
        migrations.RemoveField(
            model_name='resources',
            name='event',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.DeleteModel(
            name='TeamRegistration',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='EventDetails',
        ),
        migrations.DeleteModel(
            name='Resources',
        ),
    ]
