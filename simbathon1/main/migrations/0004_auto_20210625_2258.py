# Generated by Django 3.2.3 on 2021-06-25 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210623_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='vlog',
            name='tag',
            field=models.CharField(max_length=200, null=True),
        ),
    ]