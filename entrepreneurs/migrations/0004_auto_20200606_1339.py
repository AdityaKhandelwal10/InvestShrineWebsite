# Generated by Django 3.0.6 on 2020-06-06 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0003_auto_20200604_1523'),
        ('entrepreneurs', '0003_entrepreneurportfoliomodel_investment_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndustryModel',
            new_name='Industry',
        ),
        migrations.RenameModel(
            old_name='EntrepreneurPortfolioModel',
            new_name='PortfolioEnt',
        ),
    ]
