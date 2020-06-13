# Generated by Django 3.0.6 on 2020-06-09 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('investors', '0006_auto_20200606_1814'),
        ('entrepreneurs', '0005_auto_20200606_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolioent',
            name='email_id',
        ),
        migrations.RemoveField(
            model_name='portfolioent',
            name='userid',
        ),
        migrations.AddField(
            model_name='portfolioent',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entrepreneur_portfolio', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='industry',
            field=models.ManyToManyField(to='entrepreneurs.Industry'),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='investment_options',
            field=models.ManyToManyField(to='investors.InvestmentOptions'),
        ),
    ]