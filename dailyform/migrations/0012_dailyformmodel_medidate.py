# Generated by Django 3.2 on 2021-04-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyform', '0011_alter_dailyformmodel_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyformmodel',
            name='medidate',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=5, null=True),
        ),
    ]
