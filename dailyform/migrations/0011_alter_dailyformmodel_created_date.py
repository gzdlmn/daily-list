# Generated by Django 3.2 on 2021-04-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyform', '0010_auto_20210409_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyformmodel',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, max_length=10, null=True),
        ),
    ]
