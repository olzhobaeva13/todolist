# Generated by Django 3.2.6 on 2021-08-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_compleated',
            new_name='is_completed',
        ),
    ]