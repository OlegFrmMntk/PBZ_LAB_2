# Generated by Django 3.1.2 on 2020-10-28 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_exhibition_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='exhibition_hall',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.exhibitionhall'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='execution',
            field=models.CharField(max_length=100),
        ),
    ]
