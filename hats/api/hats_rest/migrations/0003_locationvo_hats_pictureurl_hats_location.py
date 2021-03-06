# Generated by Django 4.0.3 on 2022-06-16 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hats_rest', '0002_hats_delete_hat'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet_name', models.CharField(max_length=200)),
                ('section_number', models.PositiveSmallIntegerField()),
                ('shelf_number', models.PositiveSmallIntegerField()),
                ('import_href', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='hats',
            name='pictureurl',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='hats',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hats', to='hats_rest.locationvo'),
        ),
    ]
