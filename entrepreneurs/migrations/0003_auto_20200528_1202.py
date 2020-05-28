# Generated by Django 3.0.6 on 2020-05-28 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurs', '0002_auto_20200527_1634'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Entrepreneur',
            new_name='EntrepreneurModel',
        ),
        migrations.RenameModel(
            old_name='EntrepreneurPortfolio',
            new_name='EntrepreneurPortfolioModel',
        ),
        migrations.RenameModel(
            old_name='InvestmentPlan',
            new_name='IndustryModel',
        ),
        migrations.RenameModel(
            old_name='Industry',
            new_name='InvestmentPlanModel',
        ),
        migrations.RenameField(
            model_name='industrymodel',
            old_name='investment_range',
            new_name='industry_name',
        ),
        migrations.RenameField(
            model_name='investmentplanmodel',
            old_name='industry_name',
            new_name='investment_range',
        ),
    ]
