# Generated by Django 3.0.6 on 2020-06-06 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurs', '0004_auto_20200606_1339'),
        ('investors', '0003_auto_20200604_1523'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvestmentHistoryModel',
            new_name='History',
        ),
        migrations.RenameModel(
            old_name='InvestmentOptionsModel',
            new_name='InvestmentOptions',
        ),
        migrations.RenameModel(
            old_name='InvestorPortfolioModel',
            new_name='Portfolio',
        ),
    ]
