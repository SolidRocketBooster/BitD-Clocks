# Generated by Django 2.2.3 on 2019-09-01 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clocks', '0005_auto_20190814_2032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clock',
            old_name='clock_type',
            new_name='clock_length',
        ),
    ]
