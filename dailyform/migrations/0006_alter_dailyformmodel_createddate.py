# Generated by Django 3.2 on 2021-04-07 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyform', '0005_dailyformmodel_steps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyformmodel',
            name='createddate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
