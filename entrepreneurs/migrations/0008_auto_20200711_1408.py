# Generated by Django 3.0.6 on 2020-07-11 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurs', '0007_auto_20200612_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioent',
            name='venture_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
