# Generated by Django 4.0.3 on 2022-06-16 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0002_binvo_bin_number_binvo_bin_size_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='bin',
            new_name='bins',
        ),
    ]
