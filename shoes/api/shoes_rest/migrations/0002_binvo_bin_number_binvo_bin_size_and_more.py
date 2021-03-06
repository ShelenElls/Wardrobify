# Generated by Django 4.0.3 on 2022-06-15 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='binvo',
            name='bin_number',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='binvo',
            name='bin_size',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='binvo',
            name='closet_name',
            field=models.CharField(max_length=100),
        ),
    ]
