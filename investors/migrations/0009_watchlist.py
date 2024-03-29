# Generated by Django 3.0.6 on 2020-07-20 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrepreneurs', '0012_auto_20200716_2036'),
        ('investors', '0008_portfolio_current_occupation'),
    ]

    operations = [
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrepreneurs', models.ManyToManyField(blank=True, to='entrepreneurs.PortfolioEnt')),
                ('investor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='investors.Portfolio')),
            ],
        ),
    ]
