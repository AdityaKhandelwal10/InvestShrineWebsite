# Generated by Django 3.0.6 on 2020-06-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrepreneurportfoliomodel',
            name='linkedin_profile',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]