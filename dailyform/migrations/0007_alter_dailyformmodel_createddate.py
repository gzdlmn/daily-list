# Generated by Django 3.2 on 2021-04-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyform', '0006_alter_dailyformmodel_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyformmodel',
            name='createddate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
