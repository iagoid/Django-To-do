# Generated by Django 3.0.7 on 2020-06-15 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200614_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
