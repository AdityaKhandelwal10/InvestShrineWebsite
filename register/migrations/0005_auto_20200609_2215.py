# Generated by Django 3.0.6 on 2020-06-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20200525_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='category',
        ),
        migrations.AddField(
            model_name='user',
            name='is_investor',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
