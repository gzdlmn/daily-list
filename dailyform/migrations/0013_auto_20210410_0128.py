# Generated by Django 3.2 on 2021-04-09 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyform', '0012_dailyformmodel_medidate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyformmodel',
            name='medidate',
        ),
        migrations.AddField(
            model_name='dailyformmodel',
            name='sports',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=3, null=True),
        ),
    ]
