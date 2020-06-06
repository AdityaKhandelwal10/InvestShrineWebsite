# Generated by Django 3.0.6 on 2020-06-06 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0005_auto_20200606_1557'),
        ('entrepreneurs', '0004_auto_20200606_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioent',
            name='userid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='email_id',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='exec_summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='industry',
            field=models.ManyToManyField(blank=True, null=True, to='entrepreneurs.Industry'),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='investment',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='investment_options',
            field=models.ManyToManyField(blank=True, null=True, to='investors.InvestmentOptions'),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='linkedin_profile',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolioent',
            name='startup_summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
