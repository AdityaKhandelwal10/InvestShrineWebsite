# Generated by Django 3.0.6 on 2020-07-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0009_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='num_investments',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='investment_options',
            field=models.ManyToManyField(blank=True, to='investors.InvestmentOptions'),
        ),
    ]
